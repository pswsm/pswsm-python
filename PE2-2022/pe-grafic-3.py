import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_three_ysea: pd.DataFrame = pd.read_csv('../PE2-2022/output/incidence_rate_2021_countries.csv', sep=';', decimal=',')

df_three_ysea.query('CODE == "JPN" | CODE == "KOR" | CODE == "CHN" | CODE == "PHL"', inplace=True)
df_three_ysea.query('DISEASE == "MEASLES" & 2000 <= YEAR <= 2015', inplace=True)

sns.lineplot(
        data = df_three_ysea,
        x = 'YEAR',
        y = 'INCIDENCE_RATE',
        hue = 'NAME',
        palette = 'bright'
        )
plt.show()
