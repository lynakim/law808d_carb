import pandas as pd
import numpy as np

def retrieve_dataframe():
    df = pd.read_excel("quant_metrics.xlsx")
    dataframe = pd.DataFrame(columns=["(processgrp, metric)", "(value, std) pairs"])
    
    curr_idx = 0
    grp_metric_set = set()

    for _, row in df.iterrows():
        tup = (row["ProcessGroup"], row["Metric"])
        if tup in grp_metric_set:
            idx = dataframe.index[dataframe['(processgrp, metric)'] == tup].tolist()
            stddev = row["StdDev"]
            if stddev == 0:
                stddev = row["Value"] * 0.05
            v_s_pair = (row["Value", stddev])
            dataframe.iloc[idx[0]]['(value, std) pairs'].append(v_s_pair)
        else:
            stddev = row["StdDev"]
            if stddev == 0:
                stddev = row["Value"] * 0.05
            v_s_pair = (row["Value"], stddev)
            empty_list = []
            empty_list.append(v_s_pair)
            dataframe.iloc[curr_idx] = tup, empty_list
            curr_idx += 1
            grp_,etric_set.add(tup)
    
    return dataframe
