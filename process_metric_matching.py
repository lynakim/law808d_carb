import pandas as pd

def import_csv():  
    df = import_csv("quant_metrics.csv")
    index = list(set(df['ProcessGroup']))
    columns = list(set(df['Metric']))
    table = pd.DataFrame(index=index, columns=columns)

    for _, row in df.iterrows():
        value = row["Value"]
        stddev = row["StdDev"]
        if stddev == 0:
            stddev = value * 0.05
        table.loc[row["ProcessGroup"], row["Metric"]] = (value, stddev)
    
    return table
