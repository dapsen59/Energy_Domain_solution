import psycopg2
from sqlalchemy import create_engine
import pandas as pd

# Establish the connection using psycopg2
connection = psycopg2.connect(database="coding_challenge", user='postgres', password='postgres', host="localhost", port=5432)

# Create an SQLAlchemy engine from the psycopg2 connection
# Use the connection string directly in the create_engine function
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/coding_challenge')

# Define SQL query
sql_query = """
    SELECT "Owner_Name", COUNT(*) AS Num_Single_Family_Properties, "Property_Class"
    FROM tarrant_residential
    WHERE "Property_Class" LIKE 'A1%%'
    GROUP BY "Owner_Name", "Property_Class"
    ORDER BY Num_Single_Family_Properties DESC
    LIMIT 5;
"""

# Execute SQL query using pandas
df = pd.read_sql_query(sql_query, engine)

print("Top Five Single-Family Property Owners")
print(df)

# Close the connection when done
connection.close()

