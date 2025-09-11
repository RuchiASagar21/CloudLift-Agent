import json, sys, pathlib, re

inv_p = pathlib.Path("sample_data/inventory.json")
plan_p = pathlib.Path("sample_data/golden_plan.json")

inv = json.loads(inv_p.read_text())
plan = json.loads(plan_p.read_text())

ok = True
errors = []

# inventory app names
inv_names = {x["app_name"] for x in inv}
guardrail = plan.get("budget_guardrail_usd", 75)
allowed_instances = {"t3.nano","t3.micro","t3.small"}

# Build a lookup for RPO/RTO and db_engine
inv_map = {x["app_name"]: x for x in inv}

def err(m): 
    global ok
    ok = False; errors.append(m)

# Checks
for app in plan["apps"]:
    name = app["name"]
    if name not in inv_names:
        err(f"[name] '{name}' not found in inventory")
        continue
    inv_row = inv_map[name]

    # rpo/rto match
    rpo = app["rpo_rto"]["rpo_minutes"]
    rto = app["rpo_rto"]["rto_minutes"]
    if rpo != inv_row["rpo_min"] or rto != inv_row["rto_min"]:
        err(f"[{name}] RPO/RTO mismatch plan({rpo}/{rto}) vs inv({inv_row['rpo_min']}/{inv_row['rto_min']})")

    # budget
    if app["estimated_monthly_usd"] > guardrail:
        err(f"[{name}] over budget: {app['estimated_monthly_usd']} > {guardrail}")

    # instance type
    itype = app["target"]["compute"]["instance_type"]
    if itype not in allowed_instances:
        err(f"[{name}] unsupported instance_type '{itype}'")

    # bucket
    bucket = app["target"]["storage"]["bucket"]
    if bucket != f"cloudlift-demo-{name}":
        err(f"[{name}] bucket should be 'cloudlift-demo-{name}' got '{bucket}'")

    # DB mapping
    src_db = inv_row["db_engine"].lower()
    db = app["target"]["database"]
    if src_db in ("postgres","mysql"):
        if db["service"] != "rds" or db["engine"] != src_db:
            err(f"[{name}] DB mismatch: inventory {src_db} → expected rds/{src_db}")
    elif src_db == "sqlite":
        if db["service"] != "mock":
            err(f"[{name}] sqlite should use service='mock', not '{db['service']}'")

# uptime_slo numeric
for x in inv:
    if not isinstance(x.get("uptime_slo"), (int, float)):
        err(f"[inventory:{x['app_name']}] uptime_slo must be numeric, not {type(x.get('uptime_slo')).__name__}")

if ok:
    print("✅ Validation passed.")
else:
    print("❌ Validation failed:")
    for e in errors:
        print(" -", e)
    sys.exit(1)