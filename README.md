# Real-Time Fraud Signal Pipeline

A data engineering pipeline that ingests synthetic credit card transactions and automatically flags suspicious activity using Snowflake Dynamic Tables.

## What it does
- Generates 1,000 synthetic transactions across 50 simulated users
- Loads transaction data into Snowflake
- Uses a Dynamic Table to continuously calculate each user's average spend and standard deviation
- Flags any transaction exceeding 3 standard deviations above a user's normal spending pattern

## Tech Stack
- Python
- Snowflake (Dynamic Tables, Views)

## Pipeline Architecture
Python Generator → RAW_TRANSACTIONS → FRAUD_SIGNAL_DYN_TABLE (Dynamic Table) → FRAUD_SIGNALS (View)

## Setup

1. Clone the repo
2. Install dependencies
```bash
pip install snowflake-connector-python python-dotenv jsonlines
```
3. Create a `.env` file
SF_USER=your_username
SF_PASSWORD=your_password
SF_ACCOUNT_IDENTIFIER=your_account
4. Run the Snowflake setup SQL in `snowflake_setup.sql`
5. Generate transactions
```bash
python generate_transactions.py
```
6. Load to Snowflake
```bash
python load_to_snowflake.py
```

## How the fraud detection works
Each user builds a spending history in the Dynamic Table. When a new transaction lands that is more than 3 standard deviations above that user's average, it appears in the `FRAUD_SIGNALS` view automatically — no manual triggers needed.
