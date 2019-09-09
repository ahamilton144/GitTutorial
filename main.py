import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleveland_fed_yieldcurve.csv', sep='\t')
df.columns = ['Date','GDP_Growth','Spread_10Y_3M']
df.index = pd.to_datetime(df.Date)
del df['Date']

fig = plt.figure()
plt.plot(df)
plt.xlabel('Date')
plt.ylabel('Percentage points')
plt.legend(['GDP Growth', '10Y-3M Spread'])
plt.show()
plt.savefig('results/yieldcurve_GDP.png')

