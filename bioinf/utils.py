from pathlib import Path
from pandas import DataFrame, read_csv

def df_from_csv(csv_path: Path) -> DataFrame:
	return DataFrame(read_csv(csv_path, sep=";"))

