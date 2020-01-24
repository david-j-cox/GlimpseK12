#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
import pandas as pd
import sys
import os
import numpy as np

# Set current working directory to right folder. 
os.chdir('/Users/dcox/Dropbox/InsightFellowship/Glimpse/')

# Point to local file for custom scripts. 
sys.path.append('Users/dcox/Dropbox/Coding/Local Python Modules/')  

# Change settings to view all columns of data
pd.set_option('display.max_columns', None)

#%% Reading in the data
data_raw = pd.read_csv('GlimpseRedacted.csv')
data = data_raw.copy()
data.head()
data_cols = list(data)
data = data.replace([np.inf, -np.inf], np.nan)

#%% Checking data types
data.dtypes
    
#%%
col_nan = []
for i in data_cols:
    val = data[i].isna().sum()
    col_nan.append(val)

col_nan = pd.DataFrame(col_nan)
col_nan

#%%
for 

#%%
cols_to_int = ['GR', 'Year', 'GlimpsestudentId', \
               'Scantron Math PreTest', 'Scantron Reading PreTest', 'ScantronMath MidTest',\
               'ScantronReading MidTest', 'ScantronMathPostTest', 'ScantronReadingPostTest']
    
#%%    
for i in cols_to_int:
    data[i] = data[i].astype(int)

#%%
for i in toy_cols:
    print(i, toy_cols[i].unique())

#%% 
toy_df = data.drop(['Scantron Math PreTest', 'Scantron Reading PreTest', \
                    'ScantronMath MidTest', 'ScantronReading MidTest', \
                    'IXL Math Non User', 'IXL Math Partial User', 'IXL Math  User',\
                    'IXL Reading Non', 'IXL Reading Partial', 'IXL Reading User','num_na'], axis=1)

toy_cols = list(toy_df)

#%% Check how many nan values are missing after dropping those with > 50% missing
for i in toy_cols:
    print(i, ":", toy_df[i].isna().sum())

#%% Replace NaN values in 'type' with category 'missing'
toy_df = pd.DataFrame(toy_df)
toy_df = toy_df['Type'].fillna('Unknown', inplace=True)
toy_df.to_csv('toy_df.csv')
toy_df = pd.read_csv('toy_df.csv')

#%%##########################################################################
# PLOTS
import seaborn as sns
#%% Histogram
sns.distplot( a=col_nan, hist=True, kde=False, rug=False, bins=20)
plt.xlabel("num_nan")
plt.ylabel("num_obs")

#%% Barplot
# libraries
import numpy as np
import matplotlib.pyplot as plt

prop_val = []
for i in col_nan:
    val = i/(len(data))
    prop_val.append(val)

# Create data
height = prop_val
bars = list(data)
y_pos = np.arange(len(bars))

#%% Create bars
plt.bar(y_pos, height)
plt.xticks(y_pos, bars, rotation=90) # Rotation of the bars names
#plt.subplots_adjust(bottom=0, top=0.99) # Custom the subplot layout
plt.ylabel("prop_obs")
plt.show() # Show graphic

