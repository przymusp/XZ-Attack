import json
from clize import run

def main(push_events_file):
    with open(push_events_file, "r") as f:
        content = f.read()

        parsed_values = []
        decoder = json.JSONDecoder()

        while content:
            value, new_start = decoder.raw_decode(content)
            content = content[new_start:].strip()
            if value['actor']['login'] == 'JiaT75':
                repo = value['repo']['name']
                parsed_values.append(f"git@github.com:{repo}")

    for v in set(parsed_values):
        print(v)

if __name__ == "__main__":
    # Extract reposiotry names from Push events
    run(main)
 # One time submodule add python../scripts/get_repo_from_event.py../data_repositories/jiat75-logs/PushEvent/PushEvent.json |xargs -I {} git submodule add {}
