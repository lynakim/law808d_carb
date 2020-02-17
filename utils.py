import pandas as pd

def import_csv(filename):
    df = pd.read_csv(filename)
    return df
