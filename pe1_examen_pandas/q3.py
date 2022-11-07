# Imports
import pandas  as pd

# -----------------------------------------------------------------------------
# Student name: Pau Figueras Pavón
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: get_total_deaths()
# -----------------------------------------------------------------------------
# 
# - You are given the fixed Tycho dataset.
# - You can also use the files with solutions of question 2.
# -
# - Now, write a function that obtains all the disease that have registered
# - cases and deaths. 
# - We need to solve this question to resolve question 4, a ranking of
# - disease by death_ratio.
# 
# - Return parameters, in each function:
#   - Return a dataframe
#   - The dataframe must have 4 columns in this order: id,disease,deaths,cases
#   - 
# - Hints:
#   - 1. To make an intersection of 2 dataframe you can use merge function, using the parameter how='inner'
#   - 2. Watch the expected results in the file:
#   - tycho-q3-cases-deaths.csv
#   - 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def merge_cases_and_deaths(entries: pd.DataFrame) -> pd.DataFrame:
    df_merged_cases_and_deaths: pd.DataFrame = (entries)
    case_ranks: pd.DataFrame = df_merged_cases_and_deaths.query('event == "CASES"').groupby(by='disease').sum(numeric_only=True).drop(columns=['id', 'epi_week', 'year']).sort_values(by='number', ascending=False)
    death_ranks: pd.DataFrame = df_merged_cases_and_deaths.query('event == "DEATHS"').groupby(by='disease').sum(numeric_only=True).drop(columns=['id', 'epi_week', 'year']).sort_values(by='number', ascending=False)
    df_merged_cases_and_deaths = death_ranks.merge(right=case_ranks, how='inner', on='disease').rename(columns={"number_x":"deaths", "number_y":"cases"})
   #  df_merged_cases_and_deaths.to_csv('/tmp/merged_cases_and_deaths.csv')

    return df_merged_cases_and_deaths



# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")

    merged_cases_and_deaths:  pd.DataFrame = merge_cases_and_deaths(entries)

    print(merged_cases_and_deaths.head(10))


# -----------------------------------------------------------------------------
