#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Assumption of Regression Model :
    #Linearity: The relationship between dependent and independent variables should be linear.
    #Homoscedasticity: Constant variance of the errors should be maintained.
    #Multivariate normality: Multiple Regression assumes that the residuals are normally distributed.
    #Lack of Multicollinearity: It is assumed that there is little or no multicollinearity in the data

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load in data
data_raw = pd.read_csv('most_obs.csv')
data = data_raw.copy()

# Setup predictor and outcome variables. 
math_outc = data['ScantronMathPostTest']
math_outc = np.nan_to_num(math_outc)
read_outc = data['ScantronReadingPostTest']
read_outc = np.nan_to_num(read_outc)
predictors = data.drop(['ScantronMathPostTest', 'ScantronReadingPostTest'], axis=1)

#Setup dummy variables. 
pred_cols = list(predictors)

for i in pred_cols:
    predictors[i] = predictors[i].astype('category')
    Absolutepredictors[i] = predictors[i].cat.codes

# Splitting the dataset into the Training set and Test set for math outcome
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(predictors, math_outc, test_size=0.20, random_state=333)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("Intercept:", regressor.intercept_)
print("Slope:", regressor.coef_)

# Predicting the Test set results
from sklearn import metrics
y_pred = regressor.predict(X_test)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('R^2 Math:,', regressor.score(y_test, y_pred))

y_pred.score()


