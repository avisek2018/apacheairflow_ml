import pandas as pd

def read_csv_file():
    df = pd.read_csv('/home/avisek/airflow/datasets/heart.csv')

    print(df)

    return df.to_json()