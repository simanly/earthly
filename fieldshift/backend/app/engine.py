"""DEMO recommendation engine: transparent range-matching rules.
NOT a trained ML model. Replace `score_crops` with a real model
(e.g. scikit-learn / XGBoost) keeping the same signature."""
from .data import CROPS

def _fit(v, lo, hi):
    if lo <= v <= hi: return 1.0
    span = (hi - lo) or 1
    d = (lo - v) if v < lo else (v - hi)
    return max(0.0, 1 - d / span)

def score_crops(temp, precip, soil, prefer=None):
    out = []
    for name, c in CROPS.items():
        parts = dict(temperature=_fit(temp, *c["t"]), precipitation=_fit(precip, *c["p"]), soil_moisture=_fit(soil, *c["s"]))
        score = round(100 * (0.4*parts["temperature"] + 0.3*parts["precipitation"] + 0.3*parts["soil_moisture"]))
        weak = [k for k, v in parts.items() if v < 0.7]
        out.append(dict(crop=name, score=score, factors={k: round(v*100) for k, v in parts.items()},
                        needs=f"{c['t'][0]}-{c['t'][1]}°C, soil moisture {c['s'][0]}-{c['s'][1]}",
                        risk=("Weak match on: " + ", ".join(weak)) if weak else "No major mismatch in demo inputs",
                        note=c["note"], preferred=bool(prefer and name in prefer)))
    return sorted(out, key=lambda x: -x["score"])
