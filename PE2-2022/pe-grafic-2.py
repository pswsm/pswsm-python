import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import copy

df: pd.DataFrame = pd.read_csv('../PE2-2022/output/incidence_rate_2021_countries.csv', sep=';', decimal=',')

fdf: pd.DataFrame = df.query('CODE == "JPN" & DENOMINATOR == "per 1,000,000 total population"')

sns.boxplot(
        data = fdf,
        x = 'INCIDENCE_RATE',
        y = 'DISEASE',
        palette = 'bright',
        dodge = True
        )
plt.show()
