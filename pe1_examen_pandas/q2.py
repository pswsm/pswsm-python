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
# - Write two functions: 
# - get_total_cases
# - View the ranking of diseases by number of total cases. 
# - get_total_deaths
# - View the ranking of diseases by number of total deaths. 
# 
# - Return parameters, in each function:
#   - Return a dataframe
#   - The dataframe must have 2 columns in this order: disease, number
#   - 
# - Hints:
#   - Watch the expected results in files:
#   - tycho-q2-cases.csv
#   - tycho-q2-deaths.csv
#   - 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_total_cases(entries: pd.DataFrame) -> pd.DataFrame:
    df_total_cases: pd.DataFrame = (entries)
    case_ranks: pd.DataFrame = df_total_cases.query('event == "CASES"').groupby(by='disease').sum(numeric_only=True).drop(columns=['id', 'epi_week', 'year']).sort_values(by='number', ascending=False)
    # case_ranks.to_csv('/tmp/cases.csv')
    return case_ranks


def get_total_deaths(entries: pd.DataFrame) -> pd.DataFrame:
    df_total_deaths: pd.DataFrame = (entries)
    death_ranks: pd.DataFrame = df_total_deaths.query('event == "DEATHS"').groupby(by='disease').sum(numeric_only=True).drop(columns=['id', 'epi_week', 'year']).sort_values(by='number', ascending=False)
    # death_ranks.to_csv('/tmp/deaths.csv')
    
    return death_ranks


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")

    ranking_cases:  pd.DataFrame = get_total_cases(entries)

    ranking_deaths:  pd.DataFrame = get_total_deaths(entries)

    #print(entries.dtypes)
    print(ranking_cases, ranking_deaths)


# -----------------------------------------------------------------------------
