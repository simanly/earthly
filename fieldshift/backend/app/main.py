from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from .data import REGIONS, ALERTS, DEMO
from .engine import score_crops
from .nasa import power_daily
from .auth import router as auth_router

app = FastAPI(title="Field Shift API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:8000"],
                   allow_methods=["*"], allow_headers=["*"])

app.include_router(auth_router)

def region_or_404(rid: str):
    if rid not in REGIONS: raise HTTPException(404, "Unknown region")
    return REGIONS[rid]

@app.get("/api/health")
def health(): return dict(status="ok", mode="demo", ai_connected=False, sms_connected=False)

@app.get("/api/regions")
def regions(q: str = ""):
    return [dict(id=k, demo=DEMO, **v) for k, v in REGIONS.items() if q.lower() in v["name"].lower()]

@app.get("/api/regions/{rid}")
def region(rid: str): return dict(id=rid, demo=DEMO, **region_or_404(rid))

@app.get("/api/nasa/power/{rid}")
async def nasa_power(rid: str):
    r = region_or_404(rid)
    return await power_daily(r["lat"], r["lon"])

class RecIn(BaseModel):
    region: str
    prefer: list[str] = Field(default_factory=list)

@app.post("/api/recommend")
def recommend(body: RecIn):
    r = region_or_404(body.region)
    return dict(demo=True, engine="DEMO rule-based engine (not a trained ML model)",
                results=score_crops(r["temp"], r["precip"], r["soil"], body.prefer))

@app.get("/api/alerts")
def alerts(region: str | None = None):
    return [dict(demo=True, **a) for a in ALERTS if region in (None, a["region"])]

@app.get("/api/rankings")
def rankings(): return dict(demo=True, productivity=sorted(
    [dict(id=k, name=v["name"], prod=v["prod"]) for k, v in REGIONS.items()], key=lambda x: -x["prod"]))

class ChatIn(BaseModel):
    message: str = Field(min_length=1, max_length=500)
    region: str | None = None

@app.post("/api/chat")
def chat(body: ChatIn):
    m, tag = body.message.lower(), "[DEMO MODE: no AI model connected] "
    r = REGIONS.get(body.region or "")
    if r is None: return dict(demo=True, reply=tag + "Select a region on the map and I can answer using its demo data.")
    if any(w in m for w in ("crop", "plant", "grow")):
        top = score_crops(r["temp"], r["precip"], r["soil"])[:2]
        return dict(demo=True, reply=f"{tag}For {r['name']}, the demo engine ranks {top[0]['crop']} ({top[0]['score']}%) and {top[1]['crop']} ({top[1]['score']}%) highest.")
    if "soil" in m or "moist" in m:
        return dict(demo=True, reply=f"{tag}Demo soil moisture in {r['name']} is {r['soil']} m³/m³.")
    if "risk" in m or "alert" in m or "frost" in m:
        a = [x for x in ALERTS if x["region"] == body.region]
        return dict(demo=True, reply=tag + (f"{a[0]['type']}: {a[0]['text']} {a[0]['action']}" if a else f"No demo alerts for {r['name']}."))
    return dict(demo=True, reply=f"{tag}Try asking about crops, soil moisture, or risks in {r['name']}.")

FRONT = Path(__file__).resolve().parents[2] / "frontend"
app.mount("/", StaticFiles(directory=FRONT, html=True), name="web")
