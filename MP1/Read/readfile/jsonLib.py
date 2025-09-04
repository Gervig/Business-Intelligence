import json
import pandas as pd

__all__ = ["read_json", "write_json", "encoding_json_utf8", "pd"]

def read_json(filename) -> pd.DataFrame:
    df = pd.read_json(filename)
    return df

def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)
    return

def encoding_json_utf8(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data