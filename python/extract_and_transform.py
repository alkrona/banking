import pandas as pd

def extract_data(df)->str:
    """ extract data from csv file, """
    
    cols_new = ['transaction_id','timestamp','payee','description','raw_description','amount','balance','receipt_number']
    df=df.rename(columns={'trancode':'transaction_id'})
    #print(df.columns.tolist())
    df = df[cols_new]
    return df

def main():
    extract_data('../data/data2.csv','../data/data2.csv')
if __name__=="__main__":
    main()