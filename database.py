import sqlite3
import pandas as pd

def create_table(csv_file):
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.strip()

    table_name = csv_file.replace(".csv", "")

    df.to_sql(table_name, connection, if_exists='append', index=False)
    pass


# Estabeleça a conexão com o banco de dados
connection = sqlite3.connect('grammy.db')

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

sql_query_2 = """
CREATE TABLE IF NOT EXISTS "best-artists-rs" (
  "Rolling Stone Magazine Rank" INTEGER,
  "Artist" TEXT,
  "Racial/Ethnic group" TEXT,
  "Main Grammy awards" INTEGER,
  "Main Grammy Nominations" INTEGER,
  "Total Awards" INTEGER,
  "Total Nominations" INTEGER,
  "UK number 1's" INTEGER
);
"""

sql_query_3 = """
CREATE TABLE IF NOT EXISTS "grammys-best-record" (
  "Year" INTEGER,
  "Record" TEXT,
  "Artist" TEXT,
  "Genre" TEXT
);
"""

sql_query_4 = """
CREATE TABLE IF NOT EXISTS "grammys-best-album" (
  "Year" REAL,
  "Artist" TEXT,
  "Work" TEXT,
  "City/town of birth/origin" TEXT,
  "US State of birth/origin" TEXT,
  "Country of birth/origin" TEXT,
  "Racial/Ethnic group" TEXT
);
"""

sql_query_5 = """
CREATE TABLE IF NOT EXISTS "richest-musicians-by-year" (
  "Year" INTEGER,
  "Musician" TEXT,
  "Nationality" TEXT,
  "Earnings (Millions)" REAL,
  "Adjusted earnings
(in 2023 dollar)" INTEGER
);
"""

connection.execute(sql_query_1)
connection.execute(sql_query_2)
connection.execute(sql_query_3)
connection.execute(sql_query_4)
connection.execute(sql_query_5)

create_table("money-makers-bb.csv")
create_table("grammys-best-album.csv")
create_table("grammys-best-record.csv")
create_table("best-artists-rs.csv")
create_table("richest-musicians-by-year.csv")

connection.close()


