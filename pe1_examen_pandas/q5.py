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
# -
# - Now, write a function that save all the data of the rows that have an
# - epi_week equal to 53.
# 
# - Return parameters, in each function:
#   - Return a dataframe, with all the rows that have an epi_week equal to 53.
#   - 
# - Hints:
#   - epi_week field 2 last characters indicate the week. 
#   - One of the years which has 53 weeks is 1936.
#   - 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_rows_53_epi_week(entries: pd.DataFrame) -> pd.DataFrame:
    rows_53_epi_week: pd.DataFrame = (entries)
    #print([str(week)[4::] for week in rows_53_epi_week['epi_week'].to_list() if str(week).endswith('53')])
    rows_53_epi_week['week'] = [str(week)[4::] for week in rows_53_epi_week['epi_week'].to_list()]
    rows_53_epi_week.query("week == '53'", inplace=True)
    rows_53_epi_week.drop(columns='week', inplace=True)

    return rows_53_epi_week



# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    entries: pd.DataFrame = pd.read_csv("data/tycho-fixed.csv", sep=",")

    rows_53_epi_week:  pd.DataFrame = get_rows_53_epi_week(entries)

    print(rows_53_epi_week.head(10))



# -----------------------------------------------------------------------------
