import pandas as pd

# Read Pokedex.
pokedex: pd.DataFrame = pd.read_csv("./pokedex.csv", sep=",")

# Mask for generation
mask_gen = (pokedex.loc[:, "Generation"] == 5)

print(pokedex.loc[:, ['Generation', 'Name']] == [5])
