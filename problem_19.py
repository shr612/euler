# simple trick

import pandas as pd

rng = pd.date_range(start='1/1/1901', end='12/31/2000', freq='D')
count = 0
for date in rng:
    if date.day == 1 and date.weekday() == 6:
        count += 1
print count