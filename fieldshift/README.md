# Field Shift (NASA Space Apps 2026) — working core

Runs without any credentials. Everything labeled DEMO is illustrative, not NASA data.
Only `/api/nasa/power/{region}` calls a real NASA service (POWER, no key needed).

## Run on Windows (PowerShell)
```
cd fieldshift\backend
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000 (app) and http://127.0.0.1:8000/docs (API docs).

## Structure
- `app/data.py` demo regions, crops, alerts (replace with DB/PostGIS)
- `app/nasa.py` NASA POWER client with cache + graceful failure; add SMAP/MODIS/Landsat here
- `app/engine.py` demo rule-based recommender; swap in a trained model with the same signature
- `app/main.py` REST routes; `/api/chat` is demo mode until an AI key is wired in
- `frontend/index.html` map, region panel, crops, alerts, chat

## Added in v0.2
- Light / Dark / System theme switcher (header). Saved in the browser and, when signed in, on the account.
- Register / login (PBKDF2 hashing, signed expiring token), per-user fields (add/remove), productivity ranking panel.
- Accounts use SQLite (`fieldshift.db`) for now. Set `SECRET_KEY` in the environment for any real use.

## Not built yet
PostgreSQL/PostGIS + migrations, history/forecast page, region comparisons, farmer community/reviews,
SMS, SMAP/MODIS/Landsat, React/TypeScript/Tailwind frontend, real ML model, real AI chatbot.
