import snowflake.connector
import os
from dotenv import load_dotenv
import jsonlines

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


    with jsonlines.open("transactions.jsonl") as reader:
        for record in reader:
            cursor.execute(
                """
                INSERT INTO RAW_TRANSACTIONS 
                (transaction_id, user_id, amount, timestamp, merchant_category, city)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    record["transaction_id"],
                    record["user_id"],
                    record["amount"],
                    record["timestamp"],
                    record["merchant_category"],
                    record["city"],
                )
            )

    print("Done loading transactions.")

finally:
    cursor.close()
    conn.close()