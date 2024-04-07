#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine, text


def main():

  engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3307/db1', echo=True)

  csv_file = 'file:///etc/hosts'
  # create table etc_hosts (item string);
  table_name = 'etc_hosts'

  load_sql = f"LOAD DATA INFILE '{csv_file}' INTO TABLE {table_name} OPTIONS(delimiter = ',', mode = 'append')"

  with engine.connect() as conn:
    conn.execute(text(load_sql))

  print("CSV data loaded into MySQL table successfully!")
  

if __name__ == "__main__":
  main()
