# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:34:31 2019

@author: Niloofar-Z
"""
from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap



df2 = pd.read_csv(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\project\Pittsburgh_2.csv')

c = df2.RACE.value_counts(dropna=False)
p = df2.RACE.value_counts(dropna=False, normalize=True)
h=pd.concat([c,p*100], axis=1, keys=['counts', '%'])
h.index=['Black','White','Unkown','Hispanic or Latino','Native Hawaiian','American Native','Vietnamese-American']
## update the index but it is not smart solution :(
## smart index update is h.rename(index={'B': 'Black'....})
import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python')

####pie chart for RACE
race = np.char.array(['Black','White','Unkown','Hispanic or Latino','Native Hawaiian','American Native','Vietnamese-American'])
values = np.array([17324, 11087, 332,274, 210, 134, 8])
colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan']
porcent = 100.*values/values.sum()

patches, texts = plt.pie(values, colors=colors, startangle=90, radius=1.2)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(race, porcent)]

sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, race),
                                          key=lambda x: x[2],
                                          reverse=True))

plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

plt.savefig('foo.png', bbox_inches='tight',dpi=600)
plt.show()

#The following pie charts do not look nice

"""


df2.RACE.value_counts().plot(kind='pie',subplots=True)
plt.show()

#or

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["17341  B",
          "11094  W",
          "332  O",
          "274  H",
          "210  U",
          "134  A",
          "8  I"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))
ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="best",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Matplotlib bakery: A pie")
plt.show()

import matplotlib.pyplot as plt
import numpy as np


x = np.char.array(['Black','White','Unkown','Hispanic or Latino','Native Hawaiian','American Native','Vietnamese-American'])
y = np.array([17341, 11094, 332,274, 210, 134, 8])
colors = ['yellowgreen', 'red', 'gold', 'lightskyblue', 
          'white','lightcoral','blue','pink', 'darkgreen', 
          'yellow','grey','violet','magenta','cyan']
porcent = 100.*y/y.sum()
x = np.char.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct', 'Nov','Dec'])
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]

plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=False, 
        colors=colors, startangle=90, radius=1.2)

plt.show()

"""
