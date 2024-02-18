import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(".env")

# environment variables
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# create URL connection to sql db
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def test_read_data_and_check_schema():
    df = pd.read_sql('SELECT * FROM sales', con=DATABASE_URL)

    # Check if df is not empty
    assert not df.empty, "The Dataframe is empty."

    expected_dtype = {
        'email': 'object', 
        'date': 'datetime64[ns]',
        'value': 'float64',
        'quantity': 'int64',
        'product': 'object',
        'category': 'object'
    }
    print(df.types.to_dict)
    assert df.dtypes.to_dict() == expected_dtype, "The DataFrame schema does not match what was expected."
    #Save into database
    engine = create_engine(DATABASE_URL)
    df.to_sql('sales', con=engine, if_exists='replace', index=False)
																		  
							
			
											   
						  
											
