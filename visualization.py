# I am creating a table and a bar chart to visualize the top 10 arrest precincts by number of arrests!
import csv

# Load the data
path = "/Users/cc/Desktop/Python/Shiyi.github.io/Project 1/NYPD_Arrest_Data__Year_to_Date_.csv"
column_name = "ARREST_PRECINCT"

# Step 1: Read counts of arrests per precinct
counts = {}
with open(path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            val = int(float(row[column_name]))
            counts[val] = counts.get(val, 0) + 1
        except (ValueError, KeyError):
            continue

# Step 2: Get top 10 precincts by arrest count
top_precincts = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

# Step 3: Print as a formatted text table
print("=" * 45)
print(f"{'Rank':<5}{'Precinct':<12}{'Arrest Count':>15}")
print("=" * 45)
for i, (precinct, cnt) in enumerate(top_precincts, start=1):
    print(f"{i:<5}{precinct:<12}{cnt:>15,}")
print("=" * 45)

# Step4: Create ASCII bar chart
# take top 10 by count
top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:10]
max_count = top[0][1] if top else 0

def bar(count, max_count, width=40, fill="*"):
    if max_count == 0:
        return ""
    filled = int(round(count / max_count * width))
    return fill * filled

print("Top 10 Precincts — Arrest Counts (ASCII)")
for precinct, cnt in top:
    print(f"{precinct:>3}: {bar(cnt, max_count)} {cnt}")
