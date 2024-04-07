#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine


def main():

  engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3307/db1', echo=True)

  query = "SELECT * FROM t2"

  df = pd.read_sql(query, engine)

  print(df.head())

  

if __name__ == "__main__":
  main()
