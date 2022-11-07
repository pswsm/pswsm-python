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
#   3. Sort the dataframe by epi_week and state in alphabetical order (oldest weeks first, state order A-Z)
#   4. Add a new column called 'year' of type 'int' with the year from the epi_week.
#   5. Select rows where the years are between 1932 and 1936.
#   6. Select the rows with value 'CITY' in the column named loc_city. 
#   7. Add a new column called 'id' with a numerical unique identifier starting from 0
# 
# - Return parameters:
#   - Return the fixed entries as a dataframe.
#   - This dataframe must have this columns, in this order:
#   - ['id','epi_week', 'year', 'from_date', 'to_date', 'state', 'city', 'event', 'disease', 'number']
# 
# - Hints:
#   Step2.
#   <dataframe>.str.replace(pat=r' \[.*\]', repl='', regex=True)
#   Step5. You can use masks or this function:
#   <dataframe>.query( min_year <= year <= max_year )
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - Run pytest to be sure you succeeded.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def get_year(epi_week: int) -> int:

    epi_week_str: str = str(epi_week)
    year_str:     str = epi_week_str[0:4]
    year_int:     int = int(year_str)

    return year_int


# -----------------------------------------------------------------------------
def fix_broken_tycho(entries: pd.DataFrame) -> pd.DataFrame:
    fixed_entries: pd.DataFrame = (entries)
    fixed_entries.drop(columns=['country', 'url'], inplace=True)
    diseases: list[str] = fixed_entries['disease'].to_list()
    tidy_diseases: list[str] = [disease.split(' [', maxsplit=1)[0] for disease in diseases]
    fixed_entries['disease'] = pd.Series(tidy_diseases)
    fixed_entries.sort_values(by=['epi_week', 'state'], ascending=[True, True], inplace=True, ignore_index=True)
    fixed_entries['year'] = pd.Series([get_year(year) for year in fixed_entries['epi_week']])
    fixed_entries.query('1931 <= year <= 1936 & loc_type == "CITY"', inplace=True)
    fixed_entries['id'] = [aid for aid in range(len(fixed_entries))]
    fixed_entries = fixed_entries[['id','epi_week', 'year', 'from_date', 'to_date', 'state', 'city', 'event', 'disease', 'number']]
    fixed_entries.reset_index(drop=True, inplace=True)

    return fixed_entries


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    broken_entries: pd.DataFrame = pd.read_csv("data/tycho-broken.csv", sep=",")
    fixed_entries:  pd.DataFrame = fix_broken_tycho(broken_entries)
    
    print(fixed_entries.head(20))

# -----------------------------------------------------------------------------
