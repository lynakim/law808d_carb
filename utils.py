import pandas as pd
import numpy as np

def retrieve_dataframe():
    df = pd.read_excel("quant_metrics.xlsx")
    dataframe = pd.DataFrame(columns=["(processgrp, metric)", "(value, std) pairs"])
    
    curr_idx = 0
    grp_metric_set = set()

    for _, row in df.iterrows():
        print("row", row)
        tup = (row["ProcessGroup"], row["Metric"])
        if tup in grp_metric_set:
            idx = dataframe.index[dataframe['(processgrp, metric)'] == tup].tolist()
            stddev = row["StdDev"]
            if stddev == 0:
                stddev = row["Value"] * 0.05
            v_s_pair = (row["Value"], stddev)
            dataframe.iloc[idx[0]]['(value, std) pairs'].append(v_s_pair)
        else:
            stddev = row["StdDev"]
            if stddev == 0:
                stddev = row["Value"] * 0.05
            v_s_pair = (row["Value"], stddev)
            empty_list = []
            empty_list.append(v_s_pair)
            data = pd.DataFrame({'(processgrp, metric)': [0], '(value, std) pairs': [0]})
            dataframe = dataframe.append(data, ignore_index=True)
            dataframe.at[curr_idx, '(processgrp, metric)'] = tup
            dataframe.at[curr_idx, '(value, std) pairs'] = empty_list
            curr_idx += 1
            grp_metric_set.add(tup)
    
    return dataframe
