'''Exercici 3 - NaN Treatment'''

import pandas as pd
from pathlib import Path

def csv_fillna(csv: Path):
    '''Replaces NaN with 0'''
    the_df: pd.DataFrame = pd.read_csv(csv, sep=',')
    df_filled_nas: pd.DataFrame = the_df.fillna(value={"FLU_RISK_LEVEL": "UNKNOWN", "HOSP_FLU_ICU_WEEKLY": 0, "HOSP_FLU_ICU_CUMULATIVE": 0})
    print(df_filled_nas);


csv_fillna(Path("./na_cut_Influenza_Surveillance_Weekly.csv"))
