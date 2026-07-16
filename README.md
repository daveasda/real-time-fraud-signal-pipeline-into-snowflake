# 🕵️ Real-Time Fraud Signal Pipeline

A data engineering pipeline that ingests synthetic credit card transactions and automatically flags suspicious activity in real time — no manual triggers, no batch jobs, just continuously computed signals.

## Overview

Traditional fraud detection often relies on scheduled batch jobs that introduce lag. This project demonstrates a real-time alternative using **Snowflake Dynamic Tables**: as new transactions land, each user's rolling spend statistics are recalculated automatically, and any transaction that spikes past their normal pattern is surfaced immediately in a queryable view.

## What It Does

- Generates 1,000 synthetic transactions across 50 simulated users
- Loads transaction data into Snowflake
- Uses a Dynamic Table to continuously calculate each user's average spend and standard deviation
- Flags any transaction exceeding 3 standard deviations above a user's normal spending pattern

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Warehouse | Snowflake (Dynamic Tables, Views) |
| Config | dotenv |

## Pipeline Architecture

```
Python Generator → RAW_TRANSACTIONS → FRAUD_SIGNAL_DYN_TABLE (Dynamic Table) → FRAUD_SIGNALS (View)
```

## How the Fraud Detection Works

Each user builds a spending history inside the Dynamic Table. When a new transaction lands that is more than 3 standard deviations above that user's average, it flows automatically into the `FRAUD_SIGNALS` view — Snowflake recomputes the table incrementally, so there's no manual trigger or scheduled job involved.

## Setup

**1. Install dependencies**
```bash
pip install snowflake-connector-python python-dotenv jsonlines
```

**2. Create a `.env` file**
```
SF_USER=your_username
SF_PASSWORD=your_password
SF_ACCOUNT_IDENTIFIER=your_account
```

**3. Run the Snowflake setup SQL**
```bash
# Execute snowflake_setup.sql in your Snowflake worksheet
```

**4. Generate transactions**
```bash
python generate_transactions.py
```

**5. Load to Snowflake**
```bash
python load_to_snowflake.py
```

## Project Structure

```
real-time-fraud-signal-pipeline-into-snowflake/
├── generate_transactions.py   # Synthetic transaction generator
├── load_to_snowflake.py       # Loads data into Snowflake
├── snowflake_setup.sql        # Dynamic Table & view definitions
└── README.md
```

## Future Improvements

- Stream transactions continuously (Kafka/Snowpipe) instead of a one-shot batch load
- Add a lightweight dashboard over the `FRAUD_SIGNALS` view
- Tune the flagging threshold using labeled fraud data instead of a fixed 3-sigma rule
