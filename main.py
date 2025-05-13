import numpy as np
import pandas as pd

# Data Processing
'Step --> 1'
df = pd.DataFrame(pd.read_csv('transactions.csv'))
# print(df.head())
# print(df.isnull().sum()) # no null value in this file 
# print(df.duplicated().sum()) # no duplicate values


'Step --> 2'
income = df[df['Amount']>0]
expence = df[df['Amount']<0]
# print(expence)


'Step -->3'
grouped = df.groupby(['Date', 'Category'])['Amount'].sum()
# print(grouped)


'Step --> 4'
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.sort_values('Date')
# df.set_index('Date',inplace=True)
# monthly = df.resample('M').sum()
# weakly = df.resample('W').sum()
# print(weakly)


# 'Second Way of doing this Step--> 4'
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.sort_values('Date')
# df['Month'] = df['Date'].dt.to_period('M')
# df['Week'] = df['Date'].dt.to_period('W')
# df['Daily'] = df['Date'].dt.to_period('D')
# monthly_summary = df.groupby('Month')['Amount'].sum()
# weekly_summary = df.groupby('Week')['Amount'].sum()
# daily_summary = df.groupby('Daily')['Amount'].sum()
# # print(monthly_summary)
# print(weekly_summary)

# Calculations (NumPy + Pandas)
'Step --> 1'
# Total_income = income.sum()
# Total_expence = expence.sum()
# print(Total_expence)

'Step --> 2'
# spending = expence.groupby('Category')['Amount'].sum()
# # print(spending)

# 'Step -->3'
# daily_mean = df.groupby('Daily')['Amount'].mean()
# daily_max = df.groupby('Daily')['Amount'].max()
# daily_min = df.groupby('Daily')['Amount'].min()
# # print(daily_mean)

# 'Step --> 4'
# df['Rolling_avg'] = df['Amount'].rolling(window=3).mean()
# # print(df)

# # Simple Console Outputs
# 'Step --> 1'
# top5 = df.nlargest(5,'Amount')
# # print(top5)

'Step --> 2'
df['Date'] = pd.to_datetime(df['Date'])
expenses_df = df[df['Amount'] < 0]
daily_expenses = expenses_df.groupby('Date')['Amount'].sum()
threshold = -4000 
high_expense_days = daily_expenses[daily_expenses < threshold]
if not high_expense_days.empty:
    print("Alert! High spending on the following days:")
    print(high_expense_days)
else:
    print("No high spending days detected.")









