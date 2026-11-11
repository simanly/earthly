"""DEMO DATA. Illustrative values only, NOT NASA observations.
Coordinates are approximate city points (no invented boundaries)."""
DEMO = True
REGIONS = {
 "ganja":   dict(name="Ganja",   lat=40.68, lon=46.36, temp=14.2, precip=36, soil=0.24, prod=71, risk="High"),
 "sheki":   dict(name="Sheki",   lat=41.19, lon=47.17, temp=12.8, precip=61, soil=0.31, prod=78, risk="Low"),
 "lankaran":dict(name="Lankaran",lat=38.75, lon=48.85, temp=16.1, precip=88, soil=0.38, prod=82, risk="Medium"),
 "guba":    dict(name="Guba",    lat=41.36, lon=48.51, temp=11.0, precip=64, soil=0.29, prod=69, risk="Low"),
 "shirvan": dict(name="Shirvan", lat=39.93, lon=48.92, temp=17.4, precip=22, soil=0.16, prod=58, risk="High"),
 "barda":   dict(name="Barda",   lat=40.37, lon=47.13, temp=16.0, precip=30, soil=0.20, prod=74, risk="Medium"),
}
# ideal ranges: temp C, annual-ish precip index (mm/month), soil moisture m3/m3
CROPS = {
 "Wheat":  dict(t=(8,16),  p=(30,70), s=(0.18,0.32), note="Cool-season cereal; sensitive to late frost at heading."),
 "Cotton": dict(t=(15,24), p=(20,50), s=(0.15,0.30), note="Warm-season; needs irrigation planning in dry months."),
 "Grapes": dict(t=(12,22), p=(25,60), s=(0.15,0.30), note="Tolerates dry spells; frost at budburst is the main risk."),
 "Potato": dict(t=(8,18),  p=(50,90), s=(0.25,0.40), note="Needs steady moisture; heat stress cuts tuber yield."),
 "Hazelnut":dict(t=(10,18),p=(55,100),s=(0.25,0.40), note="Prefers humid, mild areas."),
}
ALERTS = [
 dict(id=1, type="Frost warning", region="ganja", severity="High", detected="2026-11-10",
      text="Night minimum may drop to -3°C within 48 hours.",
      action="Review crop protection and monitor field temperatures."),
 dict(id=2, type="Forecast error", region="shirvan", severity="Medium", detected="2026-11-09",
      text="Rainfall was 40% below forecast; soil moisture is low.",
      action="Consider starting irrigation earlier."),
 dict(id=3, type="Heavy rain", region="lankaran", severity="Low", detected="2026-11-08",
      text="Above-average rain expected; check drainage.",
      action="Clear field drains."),
]
