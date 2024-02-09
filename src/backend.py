import pandas as pd 
from contract import Sales
from dotenv import load_dotenv
import os

load_dotenv(".env")

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        extra_cols = set(df.colunms) - set(Sales.model_fields.keys())
        if extra_cols:
            return False, f"Extra Colunms found: {', '.join(extra_cols)}"
    
        for index, row in df.iterrows():
            try:
                _=Sales(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Error row {index + 2}: {e}")

        return True, None

    except ValueError as ve:
        return False #,str(ve)
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def excel_to_sql(df):
    df.to_sql('sales', con=DATABASE_URL, if_exists='replace', index=False)    
