import wandb
from data_util import RUNS, KEY_PREFIX
import pandas as pd
from tqdm import tqdm
import os
if __name__ == "__main__":
    api = wandb.Api()

    for run_dict in RUNS:
        if os.path.exists(f"series_data/{run_dict['mcli_name']}.tsv"):
            os.remove(f"series_data/{run_dict['mcli_name']}.tsv")
        run_uri = run_dict['wandb_url']
        print(run_dict['mcli_name'])
        try:
            run = api.run(run_uri)
            history = run.scan_history()

            train_ce = []
            lambada = []
            step = []
            dataset_rows = []
            for i, row in tqdm(enumerate(history)):
                if i % 1000 == 0:
                    print(f"row {i}")
                dataset_row = {}
                for key in KEY_PREFIX:
                    for matching_key in [k for k in row.keys() if k.startswith(key)]:
                        dataset_row[matching_key] = row[matching_key]

                dataset_rows.append(dataset_row)
            
            print(len(dataset_rows))
            df = pd.DataFrame(dataset_rows)
            df['m_params'] = run_dict['m_params']

            with open(f"series_data/{run_dict['mcli_name']}.tsv", "w") as f:
                df.to_csv(f, sep='\t', index=None)
        except Exception as e:
            print(f"Failed to get logs for {run_dict['mcli_name']}")
            continue
