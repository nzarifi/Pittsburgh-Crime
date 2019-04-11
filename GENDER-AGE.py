# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:05:01 2019

@author: Niloofar-Z
"""

from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os
os.chdir(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\project')

df = pd.read_csv(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\project\Pittsburgh.csv')
def split(column_name):
    df['year'] = pd.DatetimeIndex(df[column_name]).year
    df['month'] = pd.DatetimeIndex(df[column_name]).month
    df['day'] = pd.DatetimeIndex(df[column_name]).day
    df['hour'] = pd.DatetimeIndex(df[column_name]).hour
    df['weekday'] = pd.DatetimeIndex(df[column_name]).weekday
 
split('ARRESTTIME')
df2 = df[df['year'].isin([2016,2017,2018,2019])]
df2.to_csv("Pittsburgh_2.csv",index=False)
df2.head()
###################################################
"""

df['RACE'].unique()
df.GENDER.value_counts()
df.GENDER.value_counts(normalize=True)
RACE_dict=dict(B='African American', W='White', O='Unknown',H='Hispanic or Latino',
               U='Native Hawaiian', A='American Native ', I='Vietnamese-American' )
"""
c = df2.GENDER.value_counts(dropna=False)
p = df2.GENDER.value_counts(dropna=False, normalize=True)
pd.concat([c,p*100], axis=1, keys=['counts', '%'])
#matplotlib.use('TkAgg')matplotlib.use('TkAgg')
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["21503  Men",
          "7835  Women",
          "31  Unkown"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))
ax.legend(wedges, ingredients,
          title="Gender",
          loc="best",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Rate of Crime Based on Gender")
plt.savefig('foo.png', bbox_inches='tight',dpi=600)
plt.show()

########################################scatter plot
#the rate of crime from 2016 to 2019 for men and women and ignore unkown? 

def temp(year):
    df3 = df2[df2['year'].isin([year])]
    return df3.GENDER.value_counts()
    
temp(2019)
#not smart: run temp 4 times to get men and women freqs for each year.
#smart one: group year and gender then count them 
df2.groupby(['year','GENDER'])['year'].count()
"""
create two separate plots
df = pd.DataFrame([[2016, 3087, 1054], [2017, 8865, 3295], [2018, 7906, 2916],
                    [2019, 1645, 570]],
                   columns=['year', 'man', 'woman'])
ax1 = df.plot.scatter(x='year', y='man', c='DarkBlue')
ax1 = df.plot.scatter(x='year', y='woman', c='red')
"""


import matplotlib.pyplot as plt

x = [2016, 2017,2018,2019]
y = [3087,8865,7906,1645]
y1=[1054,3295,2916,570]

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, s=10, c='b', marker="s", label='man')
ax1.scatter(x,y1, s=15, c='r', marker="o", label='woman')
ax1.set_title("Rate of Crime Based on Gender")
plt.xlabel("Year")
plt.ylabel("Count")
plt.legend(loc='upper left')
plt.savefig('foo.png', bbox_inches='tight',dpi=600)
plt.show()
############################
#cleaning age
df2 = pd.read_csv("Pittsburgh_2.csv")
df2['AGE'].describe()
df2.count() #therefore 29369-29121=248 missing values
test=df2[df2['AGE'].isin([0,999])]
test #21 rows include '0' and '999'. so get rid of 248+ extra 21=269 rows
missing_values = [999,0," "]#automatically detects empty cells
df2 = pd.read_csv("Pittsburgh_2.csv",na_values = missing_values,usecols=['AGE','year','GENDER'])
df2['AGE'].describe() #now we have cleaned AGE

##########boxplot
fig, ax = plt.subplots(figsize=(12,8))
df2.boxplot(column=['AGE'],ax=ax)
plt.xticks(fontsize=12)
plt.savefig('Age of crime',dpi=600,ax=ax,bbox_inches='tight')
plt.show()
###################
AGES=df2['AGE']
plt.hist([AGES],color=['blue'],bins=24 ,range=(0,120))
plt.xlabel("Age")
plt.ylabel("Count")

plt.xticks(range(0,120,20))

#plt.xlim(0,13)
plt.grid(axis='y', alpha=0.75)
plt.title("Age of Crime")

plt.savefig(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\foo.png',
            bbox_inches='tight',dpi=600)
plt.show()
###################


##age_group versus year?
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
import seaborn as sns
sns.set()
import seaborn as sns    
fig, ax =plt.subplots(figsize=(10,8))
sns.factorplot(kind='box', y='AGE', x='year', hue='GENDER',
               data=df2,ax=ax,size=8,aspect=1.5,legend_out=True)

fig.savefig("foo.png")
plt.show()
###############################
def age_group(x):
    if x <20:
        return 'teens'
    if 19 < x < 41:
        return '20 to 40'
    if 40 < x < 61:
        return '41 to 60'
    else:
        return '+60'
    
df2['age_group']=df2['AGE'].apply(age_group)    
df2.age_group.value_counts

bar=df2.groupby(['year','age_group'])['year'].count().unstack('age_group')
ax=bar.plot(kind='bar', stacked=True, colormap="jet")
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    ax.annotate('{:.0f}'.format(height), (p.get_x() + .15 * width, p.get_y() + .4 * height))
    plt.xticks(fontsize=10, rotation=60)
    ax.set_title('age_group and year', fontsize=14 )
    
plt.savefig('foo.png', bbox_inches='tight',dpi=600)    
plt.show()
#############age_group vs GENDER##################
bar=df2.groupby(['GENDER','age_group'])['GENDER'].count().unstack('age_group')
ax=bar.plot(kind='bar', stacked=True, colormap="jet")
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    ax.annotate('{:.0f}'.format(height), (p.get_x() + .15 * width, p.get_y() + .4 * height))
    plt.xticks(fontsize=10, rotation=60)
    ax.set_title('age_group and year', fontsize=14 )
    
plt.savefig('foo.png', bbox_inches='tight',dpi=600)    
plt.show()
################pie chart, age_group vs GENDER######
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["2549  teens",
          "4878  41to60",
          "13209  20to40",
          "867  +60"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))
ax.legend(wedges, ingredients,
          title="Men",
          loc="best",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Rate of Crime Based on Gender")
plt.savefig('foo.png', bbox_inches='tight',dpi=600)
plt.show()


