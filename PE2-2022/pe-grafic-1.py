import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import copy

dataset: pd.DataFrame = pd.read_csv('./incidence-rate-2021-raw.csv', sep=';', decimal='.')
dataset_copy: pd.DataFrame = copy.deepcopy(dataset)
labels: set[str] = set([label for label in dataset_copy['GROUP']])

group_counts: [int] = [len(dataset_copy.query('GROUP == @group')) for group in labels]

print(group_counts)

plt.pie(group_counts, labels=labels)
plt.show()
