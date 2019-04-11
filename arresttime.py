# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:26:16 2019

@author: Niloofar-Z
"""

from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#df2 = pd.read_csv(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\project\Pittsburgh.csv', index_col=4, parse_dates=True)
df = pd.read_csv(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\project\Pittsburgh.csv')
df.head(1)
df.columns # columns names


##splitting date to year, month, day, hour
def split(column_name):
    df['year'] = pd.DatetimeIndex(df[column_name]).year
    df['month'] = pd.DatetimeIndex(df[column_name]).month
    df['day'] = pd.DatetimeIndex(df[column_name]).day
    df['hour'] = pd.DatetimeIndex(df[column_name]).hour
    df['weekday'] = pd.DatetimeIndex(df[column_name]).weekday
 
split('ARRESTTIME')
df.year.value_counts() #2005 to 2015 few data points
df[df["year"]==2015]##shows 2015

#Since we have few points from 2005 to 2015 I ignore those rows
df2 = df[df['year'].isin([2016,2017,2018,2019])]
df2['year']
"""
##I keep removed rows as well   
criterion = lambda row: row['year'] not in [2016,2017,2018,2019]
not_in = df[df.apply(criterion, axis=1)]
not_in
"""
#police work 24/7?
df.weekday.value_counts()
c = df2.weekday.value_counts(dropna=False)
p = df2.weekday.value_counts(dropna=False, normalize=True)
h=pd.concat([c,p*100], axis=1, keys=['counts', '%'])
h.rename(index={0: 'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday'
                ,4:'Friday',5:'Saturday',6:'Sunday'})

###############months of crime

import collections
MONTHS=df2['month']
test=(collections.Counter(MONTHS))
test
df.month.value_counts()
#replacing dict key
number=dict(test)
change = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr',5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
dict((change[key], value) for (key, value) in number.items())
""" replace key one by one
test['Jan'] = test[1]
del test[1] #should delete old one as well
test
"""
#####months of crime############33
plt.hist([MONTHS],color=['blue'],bins=12, range=(1,13))
plt.xlabel("Months")
plt.ylabel("Count")

plt.xticks(range(0,13))

#plt.xlim(0,13)
plt.grid(axis='y', alpha=0.75)
plt.title("Months of Crime")

plt.savefig(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\foo.png',
            bbox_inches='tight',dpi=600)
plt.show()

###############################Year of crime#########
df2.year.value_counts()


YEARS=df2['year']
n, bins, patches = plt.hist(x=YEARS, bins=8, range=(2015,2020), color='#aa0504',

                            alpha=0.75, rwidth=0.85)

plt.grid(axis='x', alpha=0.2)
plt.grid(axis='y', alpha=0.75)
#plt.xticks(np.arange(0.5, 0.7, 0.005))
plt.xlabel('Year',fontsize=12)
plt.ylabel('Frequency',fontsize=12)
plt.title('Year of crime')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.savefig(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\foo.png',
            bbox_inches='tight',dpi=600)
plt.show()

####################seasons#####################
def seasons(x):
    if x in [1,2,3]:
        return 'Winter'
    elif x in [4,5,6]:
        return 'Spring'
    elif x in [7,8,9]:
        return 'Summer'
    else:
        return 'Fall'
    
    
df2['seasons']=df['month'].apply(seasons) 
df2.seasons.value_counts()


################hours##################
df2.hour.value_counts()
HOURS=df2['hour']
n, bins, patches = plt.hist(x=HOURS, bins=24, range=(0,24), color='#aa0504',

                            alpha=0.75, rwidth=0.85)

plt.grid(axis='x', alpha=0.2)
plt.grid(axis='y', alpha=0.75)
#plt.xticks(np.arange(0.5, 0.7, 0.005))
plt.xlabel('Hours',fontsize=12)
plt.ylabel('Frequency',fontsize=12)
plt.title('Hours of the ARRESTTIME')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.savefig(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\foo.png',
            bbox_inches='tight',dpi=600)
plt.show()
#########################################
"""read the errors
df2.loc[df2['year'].map(str) +'_'+ df2['month'].map(str)]='YandM'
df2['YandM']=df2['year'].astype(str).str.cat(df2['month'], sep='_')"""

#The following lines make the string of year_month
df2['YandM'] = df2.agg('{0[year]}_{0[month]}'.format, axis=1)
#or
df2['YandM'] = df2.agg(lambda x: f"{x['year']}_{x['month']}", axis=1)

df2['YandM']
YandM
df2.YandM.value_counts()
##YandM column does not exactly in order (exp.2016-03) therefore I used date format

from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

df2 = pd.read_csv(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\project\Pittsburgh.csv', 
                                   parse_dates=['ARRESTTIME'], 
                                   na_values=['999.99'],
                                   index_col = ['ARRESTTIME'])


#turned into index ['ARRESTTIME']
df2.head()
fouryears =df2["2016-01-01" :"2019-09-30"]


fig, ax = plt.subplots(1,1)
ax.hist(fouryears.index.values, bins=50, color='orange')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m.%Y'))
plt.savefig(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\foo.png',
            bbox_inches='tight',dpi=600)
plt.show()








