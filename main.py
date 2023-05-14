import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# conn = psycopg2.connect(
#     host="localhost",
#     database="movies",
#     user="postgres",
#     password="Nasslola_09",
#     port=5432)

# def load_data(filename):
#     table_name = os.path.splitext(os.path.basename(filename))[0]  # Extract table name from file name
#     cur = conn.cursor()

#     # Open the CSV file
#     with open(filename, 'r') as f:
#         # Read the header row and remove double quotes from column names
#         header = next(f).replace('"', '').split(';')

#         # Create the table
#         create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} {';'.join(header).replace(';', ', ')}"
        

#         cur.execute(create_table_query)


#         # Iterate over the rows in the CSV file
#         for row in f:
#             # Split the row into columns
#             columns = row.replace('"', '').split(';')

#             # Insert the row into the table
#             cur.execute(f"INSERT INTO {table_name} VALUES ({', '.join('%s' % column for column in columns)})")

#     conn.commit()
#     cur.close()

directory = "C:/Users/user/Downloads/data video/movies"

# for filename in os.listdir(directory):
#     if filename.endswith(".csv"):
#         print("Loading", filename)
#         file_path = os.path.join(directory, filename)
#         load_data(file_path)



def load_data(filename):
    df = pd.read_csv(filename, on_bad_lines='skip', delimiter=';', quotechar='"')
    df.replace('"', '', regex=True, inplace=True)
    df.to_csv(filename, index=False, sep=';')
    # name = os.path.splitext(filename)[0]
    file = filename[:-4]

    engine = create_engine(f"postgresql://postgres:Nasslola_09@localhost:5432/movies")
    # print(pd.io.sql.get_schema(df, name, con=engine))
    # create the table
    df.head(n=0).to_sql(name=file, con=engine, if_exists='replace', index=False)
    # adding data to the table
    print(f"inserting {file}...")
    df.to_sql(name=file, con=engine, if_exists='append', index=False)
    


for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print("Loading", filename)
        # file_path = os.path.join(directory, filename)
        load_data(filename)
