from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import pdb

colorsPartits: list[str] = ["Red","Yellow","Orange","Purple","Blue","Pink"]
vots_lh: pd.DataFrame = pd.read_csv(Path("./csv/vots-lh-mun-2019.csv"), sep=";")
print(vots_lh)
vots_lh.loc[:, "NumVots"].plot.pie(
        labels = vots_lh.loc[:, "Partit"],
        colors = colorsPartits,
        )
plt.show()
