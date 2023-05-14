import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def load_data(filename):
    # read the csv file
    df = pd.read_csv(filename, on_bad_lines='skip', delimiter=';', quotechar='"')

    # remove the quotation marks from each words
    df.replace('"', '', regex=True, inplace=True)
    df.to_csv(filename, index=False, sep=';')

    # create the table name
    file = filename[:-4]

    # connect to the database
    engine = create_engine(f"postgresql://<user>:<password>@<host>:<port>/data")

    # create the table
    df.head(n=0).to_sql(name=file, con=engine, if_exists='replace', index=False)

    # adding data to the table
    df.to_sql(name=file, con=engine, if_exists='append', index=False)
    
# data source
directory = "/data"

# loading the data
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print("Loading", filename)
        # file_path = os.path.join(directory, filename)
        load_data(filename)
