import pandas as pd

df = pd.read_csv('./data/daily_sales_data_0.csv')
filter_df = df[df['product'] == 'pink morsel']
filter_df.to_csv('./data/daily_sales_data_0.csv',index=False)

df = pd.read_csv('./data/daily_sales_data_1.csv')
filter_df = df[df['product'] == 'pink morsel']
filter_df.to_csv('./data/daily_sales_data_1.csv',index=False)

df = pd.read_csv('./data/daily_sales_data_2.csv')
filter_df = df[df['product'] == 'pink morsel']
filter_df.to_csv('./data/daily_sales_data_2.csv',index=False)