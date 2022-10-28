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
# - Write a function to view the ranking of diseases by number of total deaths. 
# - Additionally, create a new field that calculates the percent of deaths  
# - of each diseases compared to the total of deaths in this year.
# 
# - Return parameters:
#   - Return a dataframe.
#   - The dataframe must have 4 columns in this order: ranking, disease, num_deaths, pct_deaths
#   - The ranking must start at 1
#   - The index must be numerical, starting from 0.
# 
# - Hint:
# - A Percentage is calculated by the mathematical formula of dividing the value by the sum of 
# - all the values and then multiplying the sum by 100. 
# - This is also applicable in Pandas Dataframes. 
# - The pre-defined sum() method of pandas series is used to compute the sum 
# - of all the values of a column.
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - Run pytest to make sure you succeeded.
# -----------------------------------------------------------------------------


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_total_deaths(entries: pd.DataFrame) -> pd.DataFrame:

    ranking_deaths: pd.DataFrame = (entries)
    #grouped_ranking.sort_values('num_deaths', axis='columns', ascending=False, inplace=True)
    pct_deaths = (ranking_deaths['num_deaths'] / ranking_deaths['num_deaths'].sum()) * 100
    ranking_deaths = ranking_deaths.groupby(['num_deaths', 'year'], axis='columns')
    ranking_deaths.insert(len(ranking_deaths.columns), 'pct_deaths', pct_deaths)
    ranking_deaths = ranking_deaths.sort_values(by=["num_deaths"],ascending=False)
    ranking_deaths.insert(0, 'ranking', [rank for rank in range(len(ranking_deaths))])
    ranking_deaths = ranking_deaths.loc[:,["ranking", "disease", "num_deaths", "pct_deaths"]]

    return ranking_deaths


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed22.csv", sep=",")
    
    ranking_deaths:  pd.DataFrame = get_total_deaths(entries)
    print(ranking_deaths)


# -----------------------------------------------------------------------------
