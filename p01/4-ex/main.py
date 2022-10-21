from pathlib import Path
import pandas as pd

def filter_columns(csv: Path):
    the_df: pd.DataFrame = pd.read_csv(csv)
    masked_df: pd.DataFrame = the_df.loc[the_df['HOSP_FLU_ICU_WEEKLY'] > 20, ['MMWR_WEEK', 'HOSP_FLU_ICU_WEEKLY']]
    print(masked_df)

filter_columns(Path("../cut_Influenza_Surveillance_Weekly.csv"))
