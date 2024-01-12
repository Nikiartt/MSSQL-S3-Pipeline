import pyodbc
from E_var import Settings

settings=Settings()

Server=settings.server
Database=settings.database

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      f"Server={Server};"
                      f"Database={Database};"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()

try:
    cursor.execute('''
            CREATE TABLE  Covid (
                Product_id INT IDENTITY(1,1) Primary Key,
                Date_reported DATE,
                Country_code VARCHAR(3),
                Country VARCHAR(400),
                WHO_region VARCHAR(20),
                New_cases INT,
                Cumulative_cases INT,
                New_deaths INT,
                Cumulative_deaths INT);
                ''')
except:
    pass
