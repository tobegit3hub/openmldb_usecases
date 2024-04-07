#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine


def main():

  data = {'Name': ['Alice', 'Bob', 'Charlie'],
          'Age': [25, 30, 35],
          'City': ['New York', 'San Francisco', 'Los Angeles']}
  df = pd.DataFrame(data)

  print(df)

  parquet_file_path = '/tmp/sample_data.parquet'

  df.to_parquet(parquet_file_path)

  print(f'Parquet file saved to {parquet_file_path}')

  

if __name__ == "__main__":
  main()
