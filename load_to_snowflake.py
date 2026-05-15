import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Establish connection
conn = snowflake.connector.connect(
    user=os.getenv('SF_USER'),
    password=os.getenv('SF_PASSWORD'),
    account=os.getenv('SF_ACCOUNT_IDENTIFIER'), 
    warehouse=os.getenv('SF_WAREHOUSE') ,
    database=os.getenv('SF_DATABASE') ,
    schema=os.getenv('SF_SCHEMA')  # Format: orgname-accountname
)

# Create a cursor object to execute SQL
cursor = conn.cursor()

try:
    cursor.execute("SELECT current_version()")
    one_row = cursor.fetchone()
    print(f"Connected to Snowflake version: {one_row[0]}")
finally:
    cursor.close()
    conn.close()