# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: Pau Figueras Pavón
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: fix_broken_tycho()
# -----------------------------------------------------------------------------
# 
# - You are given a broken Tycho dataset. Write a function to fix it.
# - The function fix_broken_tycho() must do the following:
#   1. Drop 'country' and 'url' columns
#   2. Cleanup the diseases removing the descriptions in square brackets, we don't need it. (See hint below)
#   3. Add a new column called 'year' of type 'int' with the year from the epi_week.
#   4. Select rows where the year is 1896, 1897, 1898.
#   5. Add a new column called 'id' with a numerical unique identifier starting from 0
#   6. Rename 'loc' to 'city', 'number' to 'num_deaths'
#   7. Reorder columns as follows: ['id', 'year', 'epi_week', 'from_date', 'to_date', 'state', 'city', 'disease', 'num_deaths']
# 
# - Return parameters:
#   - Return the fixed entries as a dataframe.
#   - The index must be numerical, starting from 0.
# 
# - Hints:
#   Step2.
#   <dataframe>.str.replace(pat=r' \[.*\]', repl='', regex=True)
#   Step4. You can use masks or this function:
#   <dataframe>.query( min_year <= year <= max_year )
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - Run pytest to be sure you succeeded.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def fix_broken_tycho(entries: pd.DataFrame) -> pd.DataFrame:
    fixed_entries: pd.DataFrame = (entries)
    edited_entries: pd.DataFrame = fixed_entries.copy()
    edited_entries.drop(columns=['country', 'url'], inplace=True)
    fixed_disease_cols: list[str] = [fxd.split(' [')[0] for fxd in edited_entries['disease'].to_list()]
    #__import__('pdb').set_trace()
    edited_entries.drop(columns='disease', inplace=True)
    edited_entries.insert(4, 'disease', fixed_disease_cols)

    # Slice each epi_week number by converting it to a string, and the again to a number. Smart B)
    edited_entries.insert(len(edited_entries.columns), 'year', [int(str(year)[0:4]) for year in edited_entries['epi_week'].to_list()])
    #__import__('pdb').set_trace()
    edited_entries = edited_entries.loc[(edited_entries['year'] == 1896) | (edited_entries['year'] == 1897) | (edited_entries['year'] == 1898)]
    edited_entries.insert(0, 'id', [int(idx) for idx in range(len(edited_entries))])
    edited_entries.rename(columns={'loc': 'city', 'number': 'num_deaths'}, inplace=True)
    sorted_entries: pd.DataFrame = edited_entries.reindex(columns=['id', 'year', 'epi_week', 'from_date', 'to_date', 'state', 'city', 'disease', 'num_deaths'])
    sorted_entries.reset_index(drop=True, inplace=True)
    #__import__('pdb').set_trace()

    return sorted_entries


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    broken_entries: pd.DataFrame = pd.read_csv("data/tycho-broken22.csv", sep=",")
    fixed_entries:  pd.DataFrame = fix_broken_tycho(broken_entries)
    
    print(fixed_entries.head(20))

# -----------------------------------------------------------------------------
