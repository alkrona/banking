import pandas as pd
import sqlite3

def connect_db():
    conn = sqlite3.connect('../data/database/commbank')
    return conn
def create_transactions_table(conn,input_file_path):
    columns = ['transaction_id', 'timestamp', 'payee', 'description', 'raw_description', 'amount', 'balance', 'receipt_number','category']
    transdf = pd.read_csv(input_file_path, index_col = None,header=None,names=columns)
    conn.execute("DROP TABLE cust_trans")
    conn.execute('''
                    CREATE TABLE cust_trans (
                        transaction_id   TEXT PRIMARY KEY NOT NULL,
                        timestamp      NUMERIC,
                        payee     TEXT,
                        description TEXT,
                        raw_description  TEXT,
                        amount  NUMERIC,
                        balance NUMERIC,
                        receipt_number TEXT,
                        category TEXT
                    );
                    ''')
    transdf.to_sql('cust_trans', conn, if_exists='append', index = False)
def upsert(conn):
    sql = '''
            INSERT INTO transactions(transaction_id, timestamp, payee, description, raw_description, amount, balance, receipt_number)
            SELECT transaction_id, timestamp, payee, description, raw_description, amount, balance, receipt_number
            FROM cust_trans 
            WHERE true 
            ON CONFLICT(transaction_id) 
            DO UPDATE SET 
                timestamp=excluded.timestamp;
                
            '''
    conn.execute(sql)
    conn.close()


def main():
    input_file_path ="../data/gold/data2.csv"
    conn = connect_db()
    create_transactions_table(conn=conn,input_file_path=input_file_path)
    upsert(conn=conn)
if __name__=="__main__":
    main()