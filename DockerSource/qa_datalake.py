
####################
#
# QUANTARMY CARNIVORE HACK FOR ZIPLINE
# BY JCX@QUANTARMY
# 2023 - ALL RIGTHS RESERVED.
###################

import pandas as pd
from os import listdir, getenv
from exchange_calendars import get_calendar
from dotenv import load_dotenv
from arcticdb import Arctic

dotenv_path = '/root/.env'
load_dotenv(dotenv_path)

endpoint = getenv("ENDPOINT")
db = getenv("DB")
access_key = getenv("ACCESS_KEY")
secret_key = getenv("SECRET_KEY")

ac = Arctic(f's3s://{endpoint}:{db}?access={access_key}&secret={secret_key}')

print('_ - _ - _ - ')
print(f'USING CREDENTIALS:')
print(f' ENDPOINT : {endpoint}')
print(f' DB : {db}')
print(f' ACCESS : {access_key}')
print(f' KEY : {secret_key}')
print('_ - _ - _ - ')
def bse_data(environ,
                  asset_db_writer,
                  minute_bar_writer,
                  daily_bar_writer,
                  adjustment_writer,
                  calendar,
                  start_session,
                  end_session,
                  cache,
                  show_progress,
                  output_dir):
    
    #symbols = ac.get_library('index.historical.composition')
    #symbols = symbols.read('GSPC.INDX').data.index.tolist()
    #symbols =  [valor + ".US" for valor in symbols]
    symbols = ['NVDA.US','MSFT.US','META.US','AMZN.US','TSLA.US']
    if not symbols:
        
        raise ValueError("No se han encontrado TICKERS en el QA DATALAKE")
        
    divs_splits = {"divs": pd.DataFrame(columns=["sid","amount","ex_date","record_date","declared_date","pay_date",]),"splits": pd.DataFrame(columns=["sid", "ratio", "effective_date"]),}
    
    metadata = pd.DataFrame(columns=('start_date','end_date','auto_close_date','symbol','exchange'))
    sessions = calendar.sessions_in_range(start_session, end_session)

    daily_bar_writer.write(process_stocks(symbols, sessions, metadata, divs_splits))

    metadata["exchange"] = "QAX"
    exchange = {'exchange': 'QAX', 'canonical_name': 'QUANTARMY BACKTEST', 'country_code': 'US'}
    exchange_df = pd.DataFrame(exchange, index = [0])



    divs_splits["divs"]["sid"] = divs_splits["divs"]["sid"].astype(int)
    divs_splits["splits"]["sid"] = divs_splits["splits"]["sid"].astype(int)
    daily_bar_writer.write(process_stocks(symbols, sessions, metadata, divs_splits))
    asset_db_writer.write(equities=metadata, exchanges=exchange_df)
    adjustment_writer.write(splits=divs_splits["splits"], dividends=divs_splits["divs"])
    
def process_stocks(symbols, sessions, metadata, divs_splits):
    my_cal = get_calendar('NYSE')
    prices = ac.get_library('prices.stocks.us.stable')
    for sid, symbol in enumerate(symbols):
        print('[QA DATALAKE CARNIVORE ] ||| Loading {}...'.format(symbol))
        df = prices.read(symbol).data
        df = df['2010':]
        start_date = df.index[0]
        end_date = df.index[-1] 
        sessions = my_cal.sessions_in_range(start_date, end_date)
        df = df[df.index.isin(sessions)]
        df = df.reindex(sessions.tz_localize(None))[start_date:end_date] #tz_localize(None)
        df.fillna(method='ffill', inplace=True)
        df.dropna(inplace=True)    
        ac_date = end_date + pd.Timedelta(days=1)
        metadata.loc[sid] = start_date, end_date, ac_date, symbol, 'QAX'

        if ac.get_library('divs.stocks.us.stable').has_symbol(symbol):
            data_divs = ac['divs.stocks.us.stable'].read(symbol).data
            data_divs = data_divs.reset_index()
            div = pd.DataFrame()
            div['ex_date'] = data_divs['date']
            div['record_date'] = data_divs['recordDate']
            div['declared_date'] = data_divs['declarationDate']
            div['pay_date'] = data_divs['paymentDate']           
            div['amount'] = data_divs['value']   
            div['sid'] = sid

            divs = divs_splits['divs']
            ind = pd.Index(range(divs.shape[0], divs.shape[0] + div.shape[0]))
            div.set_index(ind, inplace=True)
            divs_splits["divs"] = pd.concat([divs, div], axis=0)
            print('[QA DATALAKE CARNIVORE] DIVS INFO ADDED OVER',symbol)
    
        if ac.get_library('splits.stocks.us.stable').has_symbol(symbol):
            data_splits = ac['splits.stocks.us.stable'].read(symbol).data
            data_splits = data_splits.reset_index()
            split = pd.DataFrame()
            split['effective_date'] = data_splits['date']
            split['ratio'] = data_splits['split']
            split['sid'] = sid
            splits = divs_splits["splits"]
            index = pd.Index(range(splits.shape[0], splits.shape[0] + split.shape[0]))             
            split.set_index(index, inplace=True)
            divs_splits["splits"] = pd.concat([splits, split], axis=0)
            print('[QA DATALAKE CARNIVORE] SPLIT INFO ADDED OVER',symbol)
            
        yield sid, df