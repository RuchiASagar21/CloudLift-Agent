import csv, json, sys, pathlib

src = pathlib.Path("sample_data/inventory.csv")
dst = pathlib.Path("sample_data/inventory.json")

def to_num(v):
    try:
        if "." in v: return float(v)
        return int(v)
    except: return v

rows=[]
with src.open() as f:
    for row in csv.DictReader(f):
        # normalize types
        row["cpu_cores"] = to_num(row["cpu_cores"])
        row["ram_gb"] = to_num(row["ram_gb"])
        row["disk_gb"] = to_num(row["disk_gb"])
        row["db_size_gb"] = to_num(row["db_size_gb"])
        row["rpo_min"] = to_num(row["rpo_min"])
        row["rto_min"] = to_num(row["rto_min"])
        # lists
        row["ports"] = [int(p.strip()) for p in row["ports"].split(",") if p.strip()]
        row["dependencies"] = [d.strip() for d in row["dependencies"].split(",") if d.strip()]
        rows.append(row)

dst.write_text(json.dumps(rows, indent=2))
print(f"Wrote {dst} with {len(rows)} items.")
