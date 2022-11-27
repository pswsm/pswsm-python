from typing import Any
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
sns.set_theme(style="dark")


# This is the main dataframe, copies will be used in each exercise
the_df: pd.DataFrame = pd.read_csv('../../m14_practica2_uf1/datasets/na_cut_Influenza_Surveillance_Weekly.csv')

# Fix NAs
main_data_frame: pd.DataFrame = the_df.fillna(value={"FLU_RISK_LEVEL": "UNKNOWN", "HOSP_FLU_ICU_WEEKLY": 0, "HOSP_FLU_ICU_CUMULATIVE": 0})
# print(main_data_frame)

copy_df1: pd.DataFrame = main_data_frame.copy()
# print(copy_df1.loc[:, ["MMWR_WEEK", "FLU_RISK_LEVEL"]])
# print(copy_df1)
year_regex = re.compile(r"^\d{4}")
month_regex = re.compile(r"\d{2}$")
df_to_plot: pd.DataFrame = copy_df1.loc[:, ["MMWR_WEEK", "HOSP_FLU_ICU_WEEKLY", "INFLUENZA_SEASON"]]
mmwr_list: list[str] = [str(mmwr) for mmwr in df_to_plot["MMWR_WEEK"]]


year: list[Any] = [year_regex.search(e).group() for e in mmwr_list]
# print(year)


week: list[Any] = [month_regex.search(mmwr).group() for mmwr in mmwr_list]
# print(week)

df_to_plot['YEAR'] = pd.Series(year)
df_to_plot['WEEK'] = pd.Series(week)
print(df_to_plot)
sns.lineplot(data = df_to_plot.loc[:, ["WEEK", "HOSP_FLU_ICU_WEEKLY", "YEAR"]],
             x = "WEEK",
             y = "HOSP_FLU_ICU_WEEKLY",
             hue = "YEAR"
            )
plt.show()
