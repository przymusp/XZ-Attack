import json
import glob
from clize import run
import tqdm
from datetime import datetime
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

def parse_file(push_events_file):
    with open(push_events_file, "r") as f:
        content = f.read()

        parsed_values = []
        decoder = json.JSONDecoder()

        while content:
            value, new_start = decoder.raw_decode(content)
            content = content[new_start:].strip()
            if value['actor']['login'] == 'JiaT75':
                date = value['created_at']
                dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
                parsed_values.append((push_events_file.split("/")[-1].split(".")[0], dt))

    return parsed_values

def parse_event(event_file):

    events = parse_file(event_file) 
    plt.xticks(rotation=70)
    data = pd.DataFrame.from_records(events, columns=('Event', 'Date'))
    data["Date"] = pd.to_datetime(data['Date'])
    data['stime'] = data['Date'].dt.hour
    data['sdate'] = data['Date'].dt.month
    df = data.groupby(by=["stime", "sdate"]).count().reset_index().pivot(columns=["stime", "sdate"])

    sns.heatmap(data=df)
    fname = event_file.split("/")[-1].split(".")[0]
    plt.savefig(f"{fname}_timeplot.svg")
    plt.close()

def parse_all(events_dir):
    for d in tqdm.tqdm(glob.glob(f"{events_dir}/**/*.json")):
        parse_event(d)


if __name__ == "__main__":
    run(parse_all)
