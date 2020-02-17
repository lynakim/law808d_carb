import pandas as pd

def import_csv(filename):
    df = pd.read_csv(filename, encoding= 'unicode_escape')
    return df
