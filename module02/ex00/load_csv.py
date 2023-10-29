import pandas as pd
from typing import Union

def load(path: str) -> Union[pd.DataFrame, None]:
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError: 
        print('Not found this file')
        return None
    except Exception:
        print('Error lors du chargement')

def main():
    load("../population_total.csv")

if __name__ == "__main__":
    main()
