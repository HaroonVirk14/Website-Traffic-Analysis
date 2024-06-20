import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns


file_path = 'C:/Users/Haroon Virk/Downloads/Data Analysis/TSK-000-191/daily-website-visitors.csv'

data = pd.read_csv(file_path)


data['Page.Loads'] = data['Page.Loads'].str.replace(',', '').astype(int)

data['Unique.Visits'] = data['Unique.Visits'].str.replace(',', '').astype(int)

data['First.Time.Visits'] = data['First.Time.Visits'].str.replace(',', '').astype(int)

data['Returning.Visits'] = data['Returning.Visits'].str.replace(',', '').astype(int)


data['Date'] = pd.to_datetime(data['Date'])


data['Year'] = data['Date'].dt.year

data['Month'] = data['Date'].dt.month


monthly_data = data.groupby(['Year', 'Month'])[['Page.Loads', 'Unique.Visits', 'First.Time.Visits', 'Returning.Visits']].sum().reset_index()


plt.figure(figsize=(14, 7))

sns.lineplot(data=monthly_data, x='Month', y='Unique.Visits', hue='Year', palette='tab10')

plt.title('Monthly Trend of Unique Visits by Year')

plt.xlabel('Month')

plt.ylabel('Unique Visits')

plt.legend(title='Year')

plt.show()


plt.figure(figsize=(14, 7))

sns.histplot(data['Unique.Visits'], kde=True, color='blue', bins=30)

plt.title('Distribution of Unique Visits')

plt.xlabel('Unique Visits')

plt.ylabel('Frequency')

plt.show()


data['Cumulative.Unique.Visits'] = data['Unique.Visits'].cumsum()

data['Cumulative.First.Time.Visits'] = data['First.Time.Visits'].cumsum()

data['Cumulative.Returning.Visits'] = data['Returning.Visits'].cumsum()


plt.figure(figsize=(14, 7))

plt.plot(data['Date'], data['Cumulative.Unique.Visits'], label='Cumulative Unique Visits', color='blue')

plt.plot(data['Date'], data['Cumulative.First.Time.Visits'], label='Cumulative First-Time Visits', color='green')

plt.plot(data['Date'], data['Cumulative.Returning.Visits'], label='Cumulative Returning Visits', color='red')

plt.xlabel('Date')

plt.ylabel('Cumulative Visits')

plt.title('Cumulative Visits Over Time')

plt.legend()

plt.show()

data['Returning_to_First_Time_Ratio'] = data['Returning.Visits'] / data['First.Time.Visits']



plt.figure(figsize=(14, 7))

plt.plot(data['Date'], data['Returning_to_First_Time_Ratio'], label='Returning to First-Time Visits Ratio', color='purple')

plt.xlabel('Date')

plt.ylabel('Ratio')

plt.title('Ratio of Returning to First-Time Visits Over Time')

plt.legend()

plt.show()
