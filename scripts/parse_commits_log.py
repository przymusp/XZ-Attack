from collections import defaultdict
import re
from datetime import datetime
import pandas as pd

regex_date = r"Date:\s+([A-Za-z]{3} [A-Za-z]{3} \d{2} \d{2}:\d{2}:\d{2} \d{4} [+-]\d{4})"

commits = defaultdict(dict)

with open("affected_commits_xz.log", "r") as f:
    for line in f:
        match = re.search(regex_date, line)
        sl = line.strip().split(".diff")
        sha = sl[0].split("/")[-1]
        if match:
            datetime_str = match.group(1)
            datetime_format = "%a %b %d %H:%M:%S %Y %z"
            parsed_datetime = datetime.strptime(datetime_str, datetime_format)
            commits[sha]["year"] = parsed_datetime.year
            commits[sha]["month"] = parsed_datetime.month
            commits[sha]["date"] = parsed_datetime
            f.readline()
            title = f.readline().split(".diff-")[-1]
            commits[sha]["title"] = title.strip().replace(":", " ")
df = pd.DataFrame(commits).T.sort_values("date")

prev_year = 2020
prev_month = 0

ret = """
```mermaid
timeline
    title commits
    
"""

for row in df.itertuples():
    if row.year != prev_year:
        ret += f"    section {row.year}\n"
    if row.month != prev_month:
        ret += f"      {row.month:02}:"
    else:
        ret += "        :"
    if '203b008eb220208981902e0db541c02d1c1c9f5e' in row.Index:
        ret += " Gained trust"
    ret +=     f" {row.Index[:10]} {row.title}\n"
    prev_year = row.year
    prev_month = row.month

ret += """
```
"""
print(ret)


