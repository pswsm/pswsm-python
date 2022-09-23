import pandas as pd

def main():
    data: dict[str, list] = {"legs": [4, 8, 4, 0, 2, 2], "wings": [0, 0, 0, 0, 2, 2], "fly": [False, False, False, False, True, False]}
    animals: list[str] = ["panda", "spider", "horse", "snake", "duck", "penguin"]

    a_data_frame: pd.DataFrame = pd.DataFrame(data=data, index=animals)
    return a_data_frame

if __name__ == "__main__":
    df: pd.DataFrame = main()
    print(df["legs"])

