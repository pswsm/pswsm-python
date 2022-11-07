# Imports
import pandas  as pd

# Need to impor this when not running on jupyter
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Student name: Pau Figueras Pavón
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question: get_total_deaths()
# -----------------------------------------------------------------------------
# 
# - You are given the fixed Tycho dataset.
# - You can also use the solution file of question 3.
# -
# - Now, write a function that obtains the ranking of all disease that have
# - registered cases and deaths, by death_ratio.
# - The death ratio is the result of divide number of deaths by all the 
# - number of cases, multiplied by 100.
# - Finally, plot this results.
# 
# - Return parameters, in each function:
#   - Return a dataframe
#   - The dataframe must have 4 columns in this order: disease,deaths,cases,ratio_deaths
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
def get_death_ratios(entries: pd.DataFrame) -> pd.DataFrame:
    df_merged_cases_and_deaths: pd.DataFrame = (entries)
    q3_data: pd.DataFrame = pd.read_csv('./output/tycho-q3-cases-deaths.csv')
    ratios: pd.Series = pd.Series([(unalives / cases) * 100 for (unalives, cases) in zip(q3_data['deaths'], q3_data['cases'])])
    q3_data['ratio_deaths'] = ratios
    df_merged_cases_and_deaths = q3_data[['disease', 'deaths', 'cases', 'ratio_deaths']]

    return df_merged_cases_and_deaths.sort_values(by='ratio_deaths', ascending=False)



# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")

    death_ratios:  pd.DataFrame = get_death_ratios(entries)

    print(death_ratios.head(10))

    # Plot the death_ratios
    death_ratios = death_ratios.loc[:,['disease','ratio_deaths']].set_index('disease')
    death_ratios.plot(kind="barh", title="Diseases death ratio in USA (1931-1936)").get_figure().savefig("output/q4-ratio-deaths.pdf")
    plt.show()


# -----------------------------------------------------------------------------
