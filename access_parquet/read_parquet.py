#!/usr/bin/env python3

import pandas as pd

def main():

  parquet_file_path = '/tmp/sample_data.parquet'

  df = pd.read_parquet(parquet_file_path)

  print(df.head())  # Display the first few rows of the DataFrame
  

if __name__ == "__main__":
  main()
