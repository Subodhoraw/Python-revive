import numpy as np
import pandas as pd
temps = {
    'DAY':[ 'mon','Tue','wed','thu','fri','sat','Sun'],
    'high':[28,30,32,29,31,33,30],
    'low':[18,19,20,18,19,21,20]
}
df = pd.DataFrame(temps)

#calculate daily range 
df['daily_Range'] = df['high'] -df['low']

#Calculate daily range
weekly_high_range = df['high'].max() -df['high'].min()
weekly_low_range = df['low'].max() - df['low'].min()
print(df)