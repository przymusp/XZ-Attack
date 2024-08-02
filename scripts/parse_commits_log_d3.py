from collections import defaultdict
import re
from datetime import datetime, timedelta
import pandas as pd
import json

regex_date = r"Date:\s+([A-Za-z]{3} [A-Za-z]{3} \d{2} \d{2}:\d{2}:\d{2} \d{4} [+-]\d{4})"

commits = defaultdict(dict)

with open("affected_commits.log", "r") as f:
    for line in f:
        match = re.search(regex_date, line)
        sl = line.strip().split(".diff")
        sha = sl[0].split("/")[-1]
        if match:
            datetime_str = match.group(1)
            datetime_format = "%a %b %d %H:%M:%S %Y %z"
            parsed_datetime = datetime.strptime(datetime_str, datetime_format)
            # commits[sha]["year"] = parsed_datetime.year
            # commits[sha]["month"] = parsed_datetime.month
            commits[sha]["date"] = parsed_datetime
            f.readline()
            title = f.readline().split(".diff-")[-1]
            commits[sha]["title"] = title.strip().replace(":", " ")
df = pd.DataFrame(commits).T.sort_values("date")


data = [{'label': 'aa', 'data':[]}]

print('const myData = [{group: "XZ", data: [{label: "aa", data: [')

datetime_format = "%Y-%m-%dT%H:%M:%SZ"
for row in df.itertuples():
    tdelta = timedelta(minutes=10) 
    time = row.date.strftime(datetime_format)
    time2 = (row.date + tdelta).strftime(datetime_format)
    print(f"{{timeRange:[new Date('{time}'), new Date('{time2}')], val: 'merged'}},")
    # if '203b008eb220208981902e0db541c02d1c1c9f5e' in row.Index:
    #     "Gained trust"
    # print(row.date.strftime(datetime_format))

print(']}]}]')

# print(json.dumps(data))


