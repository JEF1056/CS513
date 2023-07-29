import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.mstats import winsorize

df = pd.read_csv('U:\Test\Dish.csv',sep=',')

#plt.figure(figsize=[18,5])
#plt.boxplot(df.first_appeared,vert=False)
#plt.xlabel('first_appeared')
#plt.show()

#plt.figure(figsize=[18,5])
#plt.boxplot(df.last_appeared,vert=False)
#plt.xlabel('last_appeared')
#plt.show()

df['first_appeared_modified'] = df['first_appeared'].mask((df['first_appeared'] < 1800) | (df['first_appeared'] > 2025), np.nan)
df['last_appeared_modified'] = df['last_appeared'].mask((df['last_appeared'] < 1800) | (df['last_appeared'] > 2025), np.nan)
df.to_csv('U:\Test\Dish_modified.csv', index=False)
