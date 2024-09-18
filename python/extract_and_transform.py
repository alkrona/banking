import pandas as pd

def extract_data(input_file_path:str,output_file_path:str)->str:
    """ extract data from csv file, """
    df = pd.read_csv(input_file_path)
    cols_new = ['transaction_id','timestamp','payee','description','raw_description','amount','balance','receipt_number']
    df=df.rename(columns={'trancode':'transaction_id'})
    #print(df.columns.tolist())
    df = df[cols_new]
    df.to_csv(path_or_buf=output_file_path,index=None,header=None)

def main():
    extract_data('../data/data2.csv','../data/data2.csv')
if __name__=="__main__":
    main()