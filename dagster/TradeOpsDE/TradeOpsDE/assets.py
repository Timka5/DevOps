import pandas as pd
import yfinance as yf 

from dagster import AssetExecutionContext, MetadataValue, asset


@asset
def download_from_yf():
    df = yf.Ticker('MSFT').history('1Y')
    df.to_csv('MSFT.csv')
    del df

# asset dependencies can be inferred from parameter names
@asset(deps=[download_from_yf])
def get_last_date():
    df = pd.read_csv('MSFT.csv')
    print(df.describe())