import pandas as _pandas
import csv
import os

# Expose pandas under the name "pd" (Had trouble reading pd)
pd = _pandas  

__all__ = ["pd", "read_csv_file", "write_csv_file"] 

def read_csv_file(filename, encoding="utf-8"):
    return pd.read_csv(filename, encoding=encoding)

def write_csv_file(filename, df: pd.DataFrame):
    df.to_csv(filename, index=False)