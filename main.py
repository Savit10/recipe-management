import csv
import pandas as pd

def transform_data():
        df = pd.read_csv('data.csv')
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x.upper())