import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline

# read data
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
print data.head()

# the feature are: tv, radio, newspaper
# the response: sales

# print the shape of the DataFrame
print data.shape
# there are 200 observations, thus 200 markets in the dataset

# visualize the relationship between the features 
# and the response using scatterplots

fig, axs = plt.subplots(1, 3, sharey=True)
'''
data.plot(kind='scatter', x='TV', y='Sales', ax=axs[0], figsize=(16, 8))
data.plot(kind='scatter', x='Radio', y='Sales', ax=axs[1])
data.plot(kind='scatter', x='Newspaper', y='Sales', ax=axs[2])
plt.show()
'''

# Linear regression
# y = Beta0 + Beta1 * x

# y is the response
# x is the feature
# Beta0 is the intercept
# Beta1 is the coefficient for x

# Together, Beta0 and Beta1 are called the model coefficients. To create your model, you must "learn" the values 
# of these coefficients. And once we've learned these coefficients, we can use the model to predict Sales!

# Coefficients estimated using least square criterion / sum of squared errors

import statsmodels.formula.api as smf

# create a fitted model in one line
lm = smf.ols(formula='Sales ~ TV', data=data).fit()

# print the coefficients
print lm.params
# outcome: 
# Intercept    7.032594
# TV           0.047537
# a "unit" increase in tv ad spending is associated with a 0.047537 "unit" increase in Sales
# aka an additional $1,000 spending on TV ads is associated with an increase in sales of 47.537 widgets

# Now predict sales
# Let's say $50k was spent, how much would we predict sales to be?
print 7.032594 + (0.047537 * 50000)

# OR (Statsmodels expects DataFrame)
X_new = pd.DataFrame({ 'TV': [50000] })
#print X_new.head()

print lm.predict(X_new)

# Plot the least squares line

# create a DataFrame with the minimum and maximum values of TV

X_new = pd.DataFrame({'TV': [data.TV.min(), data.TV.max()]})
print X_new.head()

# make predictions for those x values and store them
preds = lm.predict(X_new)
print preds

# first, plot the observed data
data.plot(kind='scatter', x='TV', y='Sales')
# then, plot the least squares line
plt.plot(X_new, preds, c='red', linewidth=2)
#plt.show()

# calculate the confidence interval
print lm.conf_int()

# Data should support you rejecting the null hypothesis
# so, null hypothesis is, there is no relationship between TV ad sales and Sales

# calculate the p-value
print lm.pvalues
# Intercept    1.406300e-35
# TV           1.467390e-42

# use .05 as the cutoff
# ignore the pvalue for the intercept
# Pvalue for TV is WAY less than .05, so reject the null hypothesis

# Evaluate the overall fit of the linear model:
# R-squared
# higher is better
lm.rsquared #0.611875...
# hard to say what a good Rsquared is
# good tool to compare different models

# ------------
# Multiple Linear Regression
# ------------
# using multiple features
# y = Beta0 + Beta1 * TV + Beta2 * Radio + Beta3 * Newspaper

# create a fitted model with all three features
lm = smf.ols(formula='Sales~TV + Radio + Newspaper', data=data).fit()

# print the coefficients
print lm.params
'''
Intercept    2.938889
TV           0.045765
Radio        0.188530
Newspaper   -0.001037
dtype: float64
'''
# What does that mean?
# For Radio and Newspaper ad spending
# $1000 increase in TV ad spending
# results in Sales of 45.765 widgets

lm.summary()

# Look at 
# coef
# pvalue (std error?)
# This model has a higher Rsquared, so this model provides a better fit
# to the data than one only includes TV

# ----------------
# Linear Regr with Sci-kit Learn
# ----------------

# create X and y
feature_cols = ['TV', 'Radio', 'Newspaper']
X = data[feature_cols]
y = data.Sales
# x are the features, y is the response (dep var)

# follow the usual sklearn pattern: import, instantiate, fit
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X, y)

# print intercept and coefficients
print lm.intercept_
print lm.coef_

# pair the feature names with the coefficients
zip(feature_cols, lm.coef_)

# NOTE, p-values and confidence intervals are not 
# easily accessible in sklearn
