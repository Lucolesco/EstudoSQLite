import sqlite3
import pandas as pd

def create_table(csv_file):
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.strip()
    table_name = csv_file.replace(".csv", "")
    df.to_sql(table_name, connection, if_exists='replace', index=False)
    pass


# Estabeleça a conexão com o banco de dados
connection = sqlite3.connect('schema.db')

create_table("money-makers-bb.csv")
create_table("best-artists-rs.csv")
create_table("grammys-best-record.csv")
create_table("grammys-best-album.csv")
create_table("richest-musicians-by-year.csv")

connection.close()


