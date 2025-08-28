import pandas as pd
import json
import os

def read_json(filename) -> pd.Dataframe:
    df = pd.read_json(filename)
    return df

def write_json(filename, list):
    with open(filename, 'w') as f:
        json.dump(list, f)
        return
