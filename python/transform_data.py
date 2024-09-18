import pandas as pd
import re

def transform_data(input_file_path:str,output_file_path:str)->None:
    columns = ['transaction_id', 'timestamp', 'payee', 'description', 'raw_description', 'amount', 'balance', 'receipt_number']
    df = pd.read_csv(input_file_path, index_col = None,header=None,names=columns)
    df['category']='other'
    df.loc[df['raw_description'].str.contains(r'AQUATIC', flags=re.IGNORECASE), 'category'] = 'GYM'
    df.loc[df['raw_description'].str.contains(r'Lebara', flags=re.IGNORECASE), 'category'] = 'LEBARA'
    df.loc[df['raw_description'].str.contains(r'COLES', flags=re.IGNORECASE), 'category'] = 'COLES'
    df.loc[df['raw_description'].str.contains(r'Transfer from xx0274 CommBank app', flags=re.IGNORECASE), 'category'] = 'D'
    df.loc[df['raw_description'].str.contains(r'Transfer to xx4211 CommBank app', flags=re.IGNORECASE), 'category'] = 'INVEST'
    df.loc[df['raw_description'].str.contains(r'Transfer from xx0274 CommBank app Invest', flags=re.IGNORECASE), 'category'] = 'D'
    df.loc[df['raw_description'].str.contains(r'MYKI', flags=re.IGNORECASE), 'category'] = 'MYKI'
    df.loc[df['raw_description'].str.contains(r'UBER', flags=re.IGNORECASE), 'category'] = 'UBER'
    df.loc[df['raw_description'].str.contains(r'STRIKE', flags=re.IGNORECASE), 'category'] = 'STRIKE'
    df.loc[df['raw_description'].str.contains(r'COSTCO',flags=re.IGNORECASE), 'category']='COSTCO'
    df.loc[df['raw_description'].str.contains(r'OVERDRAW',flags=re.IGNORECASE), 'category']='COMM'
    df.loc[df['raw_description'].str.contains(r'RENT',flags=re.IGNORECASE), 'category']='RENT'
    df.loc[df['raw_description'].str.contains(r'BARBER',flags=re.IGNORECASE), 'category']='BARBER'
    df.to_csv(output_file_path,header=None,index=None)

def main():
    transform_data(input_file_path="../data/data2.csv",output_file_path='../data/gold/data2.csv')
if __name__ =="__main__":
    main()