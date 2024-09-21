import psycopg2
import pandas as pd
import csv
from psycopg2 import sql
from sqlalchemy import create_engine
conn = psycopg2.connect(user="alka", password="JADDIvasu123!", host="alkronabanking.postgres.database.azure.com", port=5432, database="banking")
conn.autocommit=True


cursor = conn.cursor()

# Path to your CSV file
def create_transaction(df):
    cursor.execute(''' DROP TABLE  cust_trans;''')
    conn.commit()
    transdf = df
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cust_trans (
            transaction_id TEXT PRIMARY KEY,
            timestamp NUMERIC,
            payee TEXT,
            description TEXT,
            raw_description TEXT,
            amount NUMERIC,
            balance NUMERIC,
            receipt_number TEXT,
            category TEXT
        );
        ''')
    conn.commit()
    engine = create_engine('postgresql+psycopg2://', creator=lambda: conn)

        # Append data to table
    transdf.to_sql('cust_trans', engine, if_exists='append', index=False, method='multi')

        # Create table with explicit data types


def upsert(conn):
    sql = '''
    INSERT INTO transactions (transaction_id, timestamp, payee, description, raw_description, amount, balance, receipt_number, category)
    SELECT transaction_id, timestamp, payee, description, raw_description, amount, balance, receipt_number, category
    FROM cust_trans
    ON CONFLICT (transaction_id)
    DO UPDATE SET
        timestamp = EXCLUDED.timestamp,
        payee = EXCLUDED.payee,
        description = EXCLUDED.description,
        raw_description = EXCLUDED.raw_description,
        amount = EXCLUDED.amount,
        balance = EXCLUDED.balance,
        receipt_number = EXCLUDED.receipt_number,
        category = EXCLUDED.category;
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
def load_data_to_azurepsql(df):
    try:
            create_transaction(df=df)
            upsert(conn)
            print("Data imported and upserted successfully!")
    except Exception as e:
            print(f"An error occurred: {e}")
    finally:
            conn.close()
    """
INSERT INTO transactions 
(transaction_id, timestamp, payee, description, raw_description, amount, balance, receipt_number, category) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
"""
try:
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)  # Print each row for debugging
            cursor.execute(insert_query, row)
    
    conn.commit()
    print("Data imported successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    conn.rollback()

finally:
    cursor.close()
    conn.close()
   """