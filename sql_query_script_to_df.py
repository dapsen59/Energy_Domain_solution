import psycopg2
from sqlalchemy import create_engine
import pandas as pd

# Establish the connection using psycopg2
connection = psycopg2.connect(database="coding_challenge", user='postgres', password='backPASS1?!', host="localhost", port=5432)

# Create an SQLAlchemy engine from the psycopg2 connection
# Use the connection string directly in the create_engine function
engine = create_engine('postgresql+psycopg2://postgres:backPASS1?!@localhost:5432/coding_challenge')

# Define SQL query
sql_query = """
    SELECT TRIM("Owner_Name") AS "Owner_Name", COUNT(*) AS Num_Single_Family_Properties, "Property_Class"
    FROM tarrant_residential
    WHERE "Property_Class" LIKE 'A1%%'
    AND TRIM("Owner_Name") NOT ILIKE 'DR HORTON - TEXAS LTD%%'
    AND TRIM("Owner_Name") NOT ILIKE 'LENNAR HOMES OF TEXAS LAND & C%%'
    GROUP BY TRIM("Owner_Name"), "Property_Class"
    ORDER BY Num_Single_Family_Properties DESC
    LIMIT 5;
"""

# Execute SQL query using pandas
df = pd.read_sql_query(sql_query, engine)

print("Top Five Single-Family Property Owners")
print(df)

# Close the connection when done
connection.close()