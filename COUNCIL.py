# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:26:36 2019

@author: Niloofar-Z
"""

from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os
os.chdir(r'C:\Users\Niloofar-Z\Desktop\MetroCo\Python\project')
df2 = pd.read_csv("Pittsburgh_2.csv",
                  usecols=['COUNCIL_DISTRICT','PUBLIC_WORKS_DIVISION','ARRESTLOCATION',
                           'OFFENSES','INCIDENTLOCATION','INCIDENTNEIGHBORHOOD'])
df2.count()
##############
c = df2.COUNCIL_DISTRICT.value_counts()
p = df2.COUNCIL_DISTRICT.value_counts(normalize=True)
pd.concat([c,p*100], axis=1, keys=['counts', '%'])

c = df2.PUBLIC_WORKS_DIVISION.value_counts()
p = df2.PUBLIC_WORKS_DIVISION.value_counts(normalize=True)
pd.concat([c,p*100], axis=1, keys=['counts', '%'])
##############

##safest and worst neighborhood
amar=df2['INCIDENTNEIGHBORHOOD'].value_counts()
amar.head(5)
amar.tail(5)
######incident location
df2['ZP_arrest']=df2['ARRESTLOCATION'].apply(lambda x: x[-5:])
df2['ZP_arrest']
df2['ZP_location']=df2['INCIDENTLOCATION'].apply(lambda x: x[-5:])
arrest=list(df2['ZP_arrest'])
location=list(df2['ZP_location'])
len(location)
len(arrest)
#df.dropna(axis=0, how='any')
same_address=[i for i, j in zip(location, arrest) if i == j]
diff_address=[i for i, j in zip(location, arrest) if i != j]
len(same_address)/(len(diff_address)+len(same_address))

######offense type

df2 = pd.read_csv("Pittsburgh_2.csv",na_values ='NA'
                  ,usecols=['ARRESTLOCATION','OFFENSES','INCIDENTLOCATION'])

df2.count()#offense has 3 missing data.
#remove those three lines
df3=df2.dropna(how='any')
df3.columns
df3['OFFENSES']

########how to extrat offense code?
#####offense codes have several formats, here I explain my solution
#######First solution is long and inaccurate
####1. First try to slice messy codes from the rest of string  
df3['offense_code']=df3['OFFENSES'].apply(lambda x: x[:10])
type(df3['offense_code'])
c=list(df3['offense_code'])
len(c) #29366 values c is the list of messy codes
"""
sub = '6105(a)(1)'
any('(' in a for sub in c)"""#boolean and shows if the value exist
####2.try to separate those codes include  '(' and others which are 3 or 4 integer number
sub='('
non_integers=[s for s in c if sub in s]
integers=[s for s in c if sub not in s]
len(non_integers)
len(integers)  
#22245+7121=29366 so far we are not missing any code
cleaned_integers=[x[:4] for x in integers]
len(cleaned_integers) #we have cleaned code saved in cleaned_integers
#######trick to clean up non_integers
####3.partially remove those values that ends with letter.working with endswith()

#space sensitive.therefore prefixes must include all kind of possible ')'

prefixes=(')',')  ',') ')
cleaned_non_integers=[]
dirty_non_integers=[]
for word in non_integers[:]:
    if word.endswith(prefixes):
        cleaned_non_integers.append(word)
        #non_integers.remove(word)
    else:
        dirty_non_integers.append(word)
        
len(cleaned_non_integers) #another clean list
len(dirty_non_integers)  # mix of letters and other characters      
#6586+535=7121, correct!



cleaned2_non_integers=[]
for x in dirty_non_integers:
    for i in range(len(x)):
        if x[len(x)-i-1]!=")" :
           continue
        cleaned2_non_integers.append(x[0:(len(x)-i)])
        break
        
len(cleaned2_non_integers)   #the third clean list

####4.Now, concat three lists
final_offense_codes=cleaned_integers+cleaned_non_integers+cleaned2_non_integers
len(final_offense_codes) #correct!

import collections

counter=collections.Counter(final_offense_codes)
#print(counter) has ascending order while counter reserves location of values!!
#therefore no need to sort data:) 
print(counter)
counter
len(counter) #296 unique codes

max(counter.values()) #one code was reported 3956 times
counter.keys() #max of keys has no meaning

#The solution above is not that smart and accurate. 
#I did not keep the order of data and some codes like 541.06, 3802(d)(1)(ii),3503.B1II misrepresented  
#use the find() and optimize the solution
ltt=list(df3['OFFENSES'])
clean_code=[]
for x in range(len(ltt)) :
    #for i in range(len(x)):
    y=ltt[x].find(" ")
    clean_code.append(ltt[x][0:y])
        
len(clean_code) #includes offense code

counter_2=collections.Counter(clean_code)
print (counter_2)
len(counter_2)#312

#or more efficient
clean_code=[]
for x in ltt:
  y=x.find(" ")
  clean_code.append(x[0:y])
len(clean_code)







#exercise

 
#reverse each indivitual value and keep the location    
s = ['123456789v','abcd','3921(a) Th','13(a)(31)( ' ]
[x[::-1] for x in s]
s[::-1]    #only reverse location
[x[::-1] for x in s[::-1]]     #reverse location AND value  
            
"""            
list_1 = [['good',100, 20, 0.2],['bad', 10, 0, 0.0],['change', 1, 2, 2]]
list_1 = [item for item in list_1 if item[2] >= 5 or item[3] >= 0.3] 
 """   
    
    
    
    
    
    
    
    
    
    
    
    
