#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
import sys
import os
import pandas as pd
import pandas_profiling
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import csv

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
print(data.dtypes)

#%% Histogram of nan per row
sns.distplot( a=data['numna'], hist=True, kde=False, rug=False, color='black')
plt.xlabel("Number of Variables Missing Out of 29")
plt.ylabel("Number of Observations Out of 78213")

# Drop the numna col from end. 
data = data.drop('numna', axis=1)
data_cols=list(data)

#%% Count the number of nan per feature. 
col_nan = []
for i in data_cols:
    val = data[i].isna().sum()
    col_nan.append(val)

#%% Plot the number of nan per feature
height = col_nan
bars = list(data)
y_pos = np.arange(len(bars))

f, ax = plt.subplots(figsize=(10, 5))
plt.bar(y_pos, height, color='grey')
plt.xticks(y_pos, bars, rotation=90) # Rotation of the bars names
plt.ylabel("Number of Observations with NA Out of 78213")
plt.show() # Show graphic


#%% Here we're going to split our data into three. 
#    (1) Keep as many observations as possible and remove features with more than 50% of obs with nan. 
#    (2) Keep as many observations as possible and remove observations with a threshold of nan. 
#    (3) Keep all obs and features and dummy-code nan as missing vals.

#%% First dataset focusing on maximizimg obs. 
# Drop features where nan was 50% or higher (i.e., create df keeping as many obs as possible. )
# Keep continuous DVs. 
most_obs = data.drop(['ScantronMathPreTest', 'ScantronReadingPreTest', \
                    'ScantronMathMidTest', 'ScantronReadingMidTest', \
                    'IXLMathNonUser', 'IXLMathPartialUser', 'IXLMathUser',\
                    'IXLReadingNon', 'IXLReadingPartial', 'IXLReadingUser',\
                    'ScantronMathPreTestBenchmarks', 'ScantronReadingPreTestBenchmarks', \
                    'ScantronMathMidTestBenchmarks', 'ScantronReadingMidTestBenchmarks', \
                    'ScantronMathPostTestBenchmarks', 'ScantronReadingPostTestBenchmarks'], axis=1)
most_obs = most_obs.dropna()
most_obcols = list(most_obs)

# Keep binary DVs
most_obs_binary = data.drop(['ScantronMathPreTest', 'ScantronReadingPreTest', \
                    'ScantronMathMidTest', 'ScantronReadingMidTest', \
                    'IXLMathNonUser', 'IXLMathPartialUser', 'IXLMathUser',\
                    'IXLReadingNon', 'IXLReadingPartial', 'IXLReadingUser',\
                    'ScantronMathPreTest', 'ScantronReadingPreTest', \
                    'ScantronMathMidTest', 'ScantronReadingMidTest', \
                    'ScantronMathPostTest', 'ScantronReadingPostTest'], axis=1)

most_obs_binary_cols = list(most_obs_binary)

bin_cols_nan=[]
for i in most_obs_binary_cols:
    val = data[i].isna().sum()
    print(i, ":", val)

most_obs_binary.dropna()

# Check how many nan values are missing after dropping those with > 50% missing
for i in most_obs:
    print(i, ":", most_obs[i].isna().sum())

# Histograms of math and reading outcomes we're trying to predict
# Math
sns.distplot( a=most_obs['ScantronMathPostTest'], hist=True, rug=False, color='black')
plt.xlabel("Math Outcome Score")
plt.xlim(1500, 4000)
plt.ylabel("Number of Observations Out of 77770")

# Reading
sns.distplot( a=most_obs['ScantronReadingPostTest'], hist=True, rug=False, color='black')
plt.xlabel("Reading Outcome Score")
plt.xlim(1500, 4000)
plt.ylabel("Number of Observations Out of 77770")

most_obs_c = most_obs[most_obs.ScantronMathPostTest !=0]

# Correlation matrix of integer features. 
int_feats = ['GR', 'Year', 'GlimpsestudentId', 'ScantronMathPostTest', 'ScantronReadingPostTest']
int_data = most_obs_c[int_feats]
int_data = pd.DataFrame(int_data, columns=list(int_data))

sns.set(style="white")
# Compute the correlation matrix
corr = int_data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(7, 5))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


# Violin plots of categprical data
cat_feats = ['Course', 'SectionID', 'TNUM', 'School', 'Type', 'DistrictID']

#Math
f, ax = plt.subplots(figsize=(120, 15))
ax = sns.violinplot(x='Course', y='ScantronMathPostTest', data=most_obs_c)

f, ax = plt.subplots(figsize=(120, 15))
ax = sns.violinplot(x='SectionID', y='ScantronMathPostTest', data=most_obs_c)

f, ax = plt.subplots(figsize=(120, 15))
ax = sns.violinplot(x='TNUM', y='ScantronMathPostTest', data=most_obs_c)

f, ax = plt.subplots(figsize=(50, 15))
ax = sns.violinplot(x='School', y='ScantronMathPostTest', data=most_obs_c)

f, ax = plt.subplots(figsize=(50, 15))
ax = sns.violinplot(x='Type', y='ScantronMathPostTest', data=most_obs_c)

# Reading
f, ax = plt.subplots(figsize=(120, 15))
ax = sns.violinplot(x='Course', y='ScantronReadingPostTest', data=most_obs_c)

f, ax = plt.subplots(figsize=(120, 15))
ax = sns.violinplot(x='SectionID', y='ScantronReadingPostTest', data=most_obs_c)

f, ax = plt.subplots(figsize=(120, 15))
ax = sns.violinplot(x='TNUM', y='ScantronReadingPostTest', data=most_obs_c)

f, ax = plt.subplots(figsize=(50, 15))
ax = sns.violinplot(x='School', y='ScantronReadingPostTest', data=most_obs_c)

f, ax = plt.subplots(figsize=(50, 15))
ax = sns.violinplot(x='Type', y='ScantronReadingPostTest', data=most_obs_c)

most_obs_c.to_csv('most_obs.csv')

#%%  Alternatively we can try to keep as many features as possible and drop 
# only the rows where participants are missing a lot of data. 
nan_choice = []
for i in range(0, 30):
    most_feat = data.dropna(thresh=i)
    nan_choice.append(most_feat)

nan_choice = pd.DataFrame(nan_choice)

height = nan_choice
num_miss = list(range(0, 30))
num_miss = pd.DataFrame(num_miss)
bars = num_miss
y_pos = (len(bars)

plt.bar(y_pos, height)
plt.xticks(y_pos, bars)
plt.show()



most_feat = data.dropna(thresh=8)
len(most_feat)

for i in most_feat:
        print(i, )

#%% Replace NaN values in 'type' with category 'missing'
toy_df = pd.DataFrame(toy_df)
toy_df = toy_df['Type'].fillna('Unknown', inplace=True)
toy_df.to_csv('toy_df.csv')
toy_df = pd.read_csv('toy_df.csv')


#%% Barplot of nan per feature. 
prop_val = []
for i in col_nan:
    val = i/(len(data))
    prop_val.append(val)

# Create data
height = prop_val
bars = list(data)
y_pos = np.arange(len(bars))

plt.bar(y_pos, height, color='grey')
plt.xticks(y_pos, bars, rotation=90) # Rotation of the bars names
#plt.subplots_adjust(bottom=0, top=0.99) # Custom the subplot layout
plt.ylabel("Proportion of Sample")
plt.show() # Show graphic

#%% Specific dataframes

school_list = data['School'].unique()

for i in school_list:
    



math as function of grade
math as function of school
math as function of teacher

read as function of grade
read as function of school
read as function of teacher


for i in data_cols:
    print(i, ":", data[i].unique())











