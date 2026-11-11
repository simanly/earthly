"""Accounts, saved theme, and per-user fields. SQLite for now (see README: Postgres not yet wired)."""
import os, json, time, hmac, hashlib, base64, secrets, sqlite3
from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel, Field
from .data import REGIONS

DB = os.getenv("DB_PATH", "fieldshift.db")
SECRET = os.getenv("SECRET_KEY", "dev-only-change-me").encode()
router = APIRouter(prefix="/api")

def db():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    c.execute("PRAGMA foreign_keys=ON"); return c

def init():
    with db() as c:
        c.executescript("""
        create table if not exists users(id integer primary key, email text unique not null,
          name text not null, phone text, pw text not null, theme text not null default 'system');
        create table if not exists fields(id integer primary key,
          user_id integer not null references users(id) on delete cascade,
          name text not null, region text not null, crop text, area_ha real);""")
init()

def hash_pw(pw, salt=None):
    salt = salt or secrets.token_hex(8)
    return f"{salt}${hashlib.pbkdf2_hmac('sha256', pw.encode(), salt.encode(), 200_000).hex()}"

def check_pw(pw, stored):
    return hmac.compare_digest(hash_pw(pw, stored.split("$")[0]), stored)

def b64(b): return base64.urlsafe_b64encode(b).decode().rstrip("=")
def make_token(uid):
    body = b64(json.dumps({"uid": uid, "exp": int(time.time()) + 7*86400}).encode())
    return f"{body}.{b64(hmac.new(SECRET, body.encode(), hashlib.sha256).digest())}"

def user(authorization: str = Header(default="")):
    try:
        body, sig = authorization.removeprefix("Bearer ").split(".")
        good = b64(hmac.new(SECRET, body.encode(), hashlib.sha256).digest())
        if not hmac.compare_digest(sig, good): raise ValueError
        p = json.loads(base64.urlsafe_b64decode(body + "=" * (-len(body) % 4)))
        if p["exp"] < time.time(): raise ValueError
        with db() as c: row = c.execute("select * from users where id=?", (p["uid"],)).fetchone()
        if not row: raise ValueError
        return row
    except Exception:
        raise HTTPException(401, "Not signed in")

EMAIL = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
class Reg(BaseModel):
    email: str = Field(pattern=EMAIL, max_length=120)
    password: str = Field(min_length=8, max_length=100)
    name: str = Field(min_length=1, max_length=80)
    phone: str | None = Field(default=None, max_length=30)
class Login(BaseModel):
    email: str; password: str
class ThemeIn(BaseModel):
    theme: str = Field(pattern="^(light|dark|system)$")
class FieldIn(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    region: str
    crop: str | None = Field(default=None, max_length=40)
    area_ha: float | None = Field(default=None, gt=0, lt=100000)

def public(u): return dict(id=u["id"], email=u["email"], name=u["name"], phone=u["phone"], theme=u["theme"])

@router.post("/auth/register", status_code=201)
def register(b: Reg):
    try:
        with db() as c:
            cur = c.execute("insert into users(email,name,phone,pw) values(?,?,?,?)",
                            (b.email.lower(), b.name, b.phone, hash_pw(b.password)))
    except sqlite3.IntegrityError:
        raise HTTPException(409, "Email already registered")
    return dict(token=make_token(cur.lastrowid))

@router.post("/auth/login")
def login(b: Login):
    with db() as c: u = c.execute("select * from users where email=?", (b.email.lower(),)).fetchone()
    if not u or not check_pw(b.password, u["pw"]): raise HTTPException(401, "Wrong email or password")
    return dict(token=make_token(u["id"]))

@router.get("/me")
def me(u=Depends(user)): return public(u)

@router.put("/me/theme")
def set_theme(b: ThemeIn, u=Depends(user)):
    with db() as c: c.execute("update users set theme=? where id=?", (b.theme, u["id"]))
    return dict(theme=b.theme)

@router.get("/fields")
def fields(u=Depends(user)):
    with db() as c: return [dict(r) for r in c.execute("select * from fields where user_id=? order by id", (u["id"],))]

@router.post("/fields", status_code=201)
def add_field(b: FieldIn, u=Depends(user)):
    if b.region not in REGIONS: raise HTTPException(422, "Unknown region")
    with db() as c:
        cur = c.execute("insert into fields(user_id,name,region,crop,area_ha) values(?,?,?,?,?)",
                        (u["id"], b.name, b.region, b.crop, b.area_ha))
    return dict(id=cur.lastrowid, **b.model_dump())

@router.delete("/fields/{fid}", status_code=204)
def del_field(fid: int, u=Depends(user)):
    with db() as c:
        if c.execute("delete from fields where id=? and user_id=?", (fid, u["id"])).rowcount == 0:
            raise HTTPException(404, "Field not found")
