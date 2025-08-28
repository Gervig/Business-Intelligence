import pandas as pd
import json
import os

__all__ = ["read_json", "write_json", "pd", "encoding_json_utf8"]   # makes pd accessible outside

def read_json(filename) -> pd.DataFrame:
    df = pd.read_json(filename)
    return df

def write_json(filename, list):
    with open(filename, 'w') as f:
        json.dump(list, f)
        return

def encoding_json_utf8(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data