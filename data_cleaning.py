import pandas as pd
import numpy as np
from exceptions import DataCleaningError

def clean_covid_data(file_path):
    try:
        print("Data Cleaning Process:")
        df = pd.read_csv(file_path)
        print(df)    
        print( "\nNull values are:\n","\n",df.isna().sum())  
        print("\nDuplicate values are:", df.duplicated().sum()) 
        df = df.fillna(value=0)   
        print("\n",df)
        print("\nEnsuring all datatype:") 
        for col in df.columns:
             if df[col].dtypes=='int64':
                df[col]=df[col].astype('float64')
        print(df.dtypes)
        print("\n",df)  
        return df

    except KeyError as e:
        raise DataCleaningError(f"Critical column missing: {e}")
    except Exception as e:
        raise DataCleaningError(f"Error occurred during data cleaning: {e}")
