import argparse
import pandas as pd
import json
from sqlalchemy import create_engine


def write_activity_sqllite(df, sql_db, tbl_name):
  # Create sqlite engine
  engine = create_engine("sqlite:///"+sql_db)
  # Write dataframe to sqlite db
  try:
    df.to_sql(name = tbl_name, con = engine, if_exists = "replace", index = True)
  except ValueError:
    print("Pandas coulnt not write to SQLite.")
  # Check if tbl created successfully
  # query = """ SELECT * FROM %s """ % tbl_name
  # res = pd.read_sql(query, engine)
  # print(res.head())
  # sqlite3 ./activities.db

def read_activity_json(file_name):
  # Load json record-oriented
  with open(file_name) as f:
    data = json.load(f)
  # Flatten the json object
  try:
    df = pd.json_normalize(data, sep="_", max_level=1)
    return df
  except ValueError:
    print("Pandas could not parse the JSON file.")


def run(argv=None):
  # Arguments parsing
  parser = argparse.ArgumentParser()
  parser.add_argument('-input', required=True, default="activities.json", help="Activities file name.")
  parser.add_argument('-db', required=False, default="activities.db", help="SQLLite database name.")
  parser.add_argument('-tbl_name', required=False, default="ticket_activities", help="SQLite table name destination.")
  known_args = parser.parse_args(argv)
  # Read json file
  df = read_activity_json(known_args.input)
  # Write json to SQLLite db
  write_activity_sqllite(df, known_args.db, known_args.tbl_name)


# ### Main fucntion ### #
if __name__ == "__main__":
  run()