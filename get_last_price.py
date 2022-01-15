import eikon as ek

# Set Eikon App Key
ek.set_app_key('DEFAULT_CODE_BOOK_APP_KEY')

def get_price_close(ric_list, date):
    '''
    Downloads close price for specific RIC code and date
        
    Args:
        ric_list: list with the asset ric codes
        date: price close date to be downloaded
    Returns:
        df: df with price close per asset RIC
        err: error answer from Eikon API
    '''
    # Request data
    df, err = ek.get_data(instruments = ric_list, 
                          fields = 'TR.PriceClose',
                          parameters = {'SDate': date})
    # Change column name to the specific date
    return df, err


df, err = get_price_close(ric_list = ['MNST.OQ', 'TROW.OQ'], date = '20190307')
