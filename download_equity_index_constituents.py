import pandas as pd
import eikon as ek
import numpy as np
from tqdm.notebook import tqdm

# Set Eikon App Key
ek.set_app_key('DEFAULT_CODE_BOOK_APP_KEY')

# Eikon Index RIC
index_ric = '.SPX'

# Fields list: We will downdload RIC and Name of the index consituents
fields_list = ['TR.IndexConstituentRIC', 'TR.ETPConstituentName']

'''
IMPORTANT: Have in mind that Eikon API for python has a limit on the historical data you can request. 
As far as I know, limit date is on year 2015. 
'''
# Start date
start_date = '20160101'

# Create a funtion to recurrently use this code for different equity indexes and starting dates
def get_index(index_ric, fields_list, start_date):
    '''
    Downloads equity index consituents on a specific date
    
    Args:
        index_ric: Eikon Index RIC
        feilds_list: list with fields code to be downloaded
        start_date: date on which index constituents will be downloaded
    Returns:
        index_df: df with Constituent RIC and Names
    '''
    index_df= ek.get_data(instruments = index_ric, 
                          fields = fields_list,
                          parameters = {'SDate': start_date})[0]
    return index_df

'''
In some cases, Eikon Api does not return data for correct requests. Please make
sure that for any requests you run on your code, you try more than once if you 
receive no data back. '''

# Create DataFrame for our index constituents
index_df = pd.DataFrame()
# Create object where we will save the number of iterations
count = 0
# While DF lenght is smaller than one (Eikon Api answer is empty), we'll send another request
while len(index_df) <= 1:
    # Send request
    index_df = get_index(index_ric, fields_list, start_date)
    # Fix the maximum number of requesto to two
    if count == 2:
        print('We could not download equity index constituents for date', start_date)
        break
    count += 1
