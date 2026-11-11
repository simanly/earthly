"""Real NASA POWER client (no key needed). Never fabricates data:
on failure it returns available=False."""
import time, datetime as dt, httpx
_cache: dict = {}
TTL = 6 * 3600
URL = "https://power.larc.nasa.gov/api/temporal/daily/point"

async def power_daily(lat: float, lon: float, days: int = 14):
    key = (round(lat, 2), round(lon, 2), days)
    hit = _cache.get(key)
    if hit and time.time() - hit[0] < TTL:
        return hit[1]
    end = dt.date.today() - dt.timedelta(days=3)  # POWER lags a few days
    start = end - dt.timedelta(days=days)
    params = dict(parameters="T2M,PRECTOTCORR", community="AG", latitude=lat,
                  longitude=lon, start=start.strftime("%Y%m%d"),
                  end=end.strftime("%Y%m%d"), format="JSON")
    try:
        async with httpx.AsyncClient(timeout=20) as c:
            r = await c.get(URL, params=params)
            r.raise_for_status()
        p = r.json()["properties"]["parameter"]
        series = [dict(date=d, temp_c=None if v == -999 else v,
                       precip_mm=None if p["PRECTOTCORR"].get(d, -999) == -999 else p["PRECTOTCORR"][d])
                  for d, v in p["T2M"].items()]
        out = dict(available=True, source="NASA POWER (live)", fetched=dt.datetime.utcnow().isoformat()+"Z", series=series)
    except Exception as e:
        out = dict(available=False, source="NASA POWER", error=str(e)[:120])
    if out["available"]:
        _cache[key] = (time.time(), out)
    return out
