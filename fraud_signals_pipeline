-- Create dedicated objects for this project
CREATE DATABASE IF NOT EXISTS FRAUD_SIGNAL_DB;
CREATE SCHEMA IF NOT EXISTS FRAUD_SIGNAL_DB.FRAUD_SIGNAL_DATA;

-- A small virtual warehouse (compute cluster)
-- X-SMALL is free-tier friendly; suspends after 1 min idle
CREATE WAREHOUSE IF NOT EXISTS FRAUD_SIGNAL_WH
  WITH WAREHOUSE_SIZE = 'X-SMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

USE DATABASE FRAUD_SIGNAL_DB;
USE SCHEMA FRAUD_SIGNAL_DATA;
USE WAREHOUSE FRAUD_SIGNAL_WH;

CREATE TABLE IF NOT EXISTS RAW_TRANSACTIONS (
    transaction_id    VARCHAR,
    user_id           VARCHAR,
    amount            FLOAT,
    timestamp         TIMESTAMP_NTZ,
    merchant_category VARCHAR,
    city              VARCHAR
);

SELECT * FROM RAW_TRANSACTIONS LIMIT 10;

CREATE DYNAMIC TABLE FRAUD_SIGNAL_DYN_TABLE
    LAG = '1 minute'
    WAREHOUSE = FRAUD_SIGNAL_WH
    AS
    SELECT 
        user_id,
        AVG(amount) AS avg_amount,
        STDDEV(amount) AS stddev_amount
    FROM RAW_TRANSACTIONS
    GROUP BY user_id;

SELECT * FROM FRAUD_SIGNAL_DYN_TABLE;

INSERT INTO RAW_TRANSACTIONS VALUES
('txn-fraud-001', 'user_01', 9999.99, '2026-06-01 10:00:00', 'electronics', 'New York'),
('txn-fraud-002', 'user_05', 8500.00, '2026-06-01 11:00:00', 'travel', 'Los Angeles'),
('txn-fraud-003', 'user_12', 7200.50, '2026-06-01 12:00:00', 'electronics', 'Chicago');

CREATE VIEW FRAUD_SIGNALS AS
SELECT 
    RAW.transaction_id,
    RAW.user_id,
    RAW.amount,
    RAW.timestamp,
    RAW.merchant_category,
    RAW.city,
    DYN.avg_amount,
    DYN.stddev_amount
FROM RAW_TRANSACTIONS AS RAW
JOIN FRAUD_SIGNAL_DYN_TABLE AS DYN ON RAW.user_id = DYN.user_id
WHERE RAW.amount > DYN.avg_amount + (3 * DYN.stddev_amount);

SELECT * FROM FRAUD_SIGNALS;
