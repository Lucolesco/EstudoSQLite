import sqlite3
import pandas as pd

def create_table(csv_file):
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.strip()

    table_name = csv_file.replace(".csv", "")

    df.to_sql(table_name, connection, if_exists='append', index=False)
    pass


# Estabeleça a conexão com o banco de dados
connection = sqlite3.connect('trabalho.db')

# Defina o SQL para criar a tabela se ela não existir
sql_query_1 = """
CREATE TABLE IF NOT EXISTS "money-makers-bb" (
  "Artist" TEXT,
  "total" REAL,
  "sales" REAL,
  "streaming" REAL,
  "publishing" REAL,
  "touring" REAL,
  "year" INTEGER
);
"""

connection.execute(sql_query_1)

create_table("money-makers-bb.csv")


connection.close()


