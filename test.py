

import numpy as np #linear algebra
import pandas as pd #data processing, CSV file I/O (eg. pd.read_csv)
from pandas import Series, DataFrame
import matplotlib.pyplot as plt #for plots
#%matplotlib inline
import seaborn as sns #for advance plots and graphs

#Ignore Warnings
import warnings
warnings.filterwarnings("ignore")

#to view all columns
from IPython.display import display
pd.options.display.max_columns = None #?

#input data files are available in the "../data/" directory.
#for example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory)
import os
for dirname, _, filenames in os.walk('/home/hadoop/Desktop/data/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#read data
train = pd.read_csv('/home/hadoop/Desktop/data/train.csv')
test = pd.read_csv('/home/hadoop/Desktop/data/test.csv')

#combine train and test data set
data = pd.concat([train, test],ignore_index=True, sort=False)

print('the shape of  train dataset', train.shape)
print('the shape of  test dataset', test.shape)
print('the shape of  data', data.shape)

train.head()
train.tail()
data.info()
data.describe().T

#'Id' has no relation with sale price. so drop 'Id' column
train.drop(['Id'], axis=1, inplace=True)
test.drop(['Id'], axis=1, inplace=True)

#Now start EDA, first check target column is 'Sale price'
sns.distplot(train['SalePrice'])
plt.show()

print("Skewness in SalePrice :", train['SalePrice'].skew())
print("Kurtosis in SalePrice :", train['SalePrice'].kurt())

sns.boxplot(train['SalePrice'])
plt.show()

#target column is right skwed. So log transformation is requried
train['SalePrice'] = np.log(train["SalePrice"]+1)
#check distribution after log transform.
sns.distplot(train['SalePrice'])
plt.show()



# now move on toward the predictors.
# check correlation in features
cor = train.corr()
plt.figure(figsize=(15,10))
sns.heatmap(cor,cmap="Blues", vmax=0.9)
plt.show()

# checking high correlational features to 'Saleprice'
cor[abs(cor['SalePrice'].values) >= 0.5]['SalePrice'].sort_values(ascending=False)[1:] #?


#so this features have good correlation with target variable
#so check this their now realtion
#over11qual is catagorical feature so draw boxplot
fig = plt.figure(constrained_layout=True, figsize=(8,5))
sns.boxplot(train['OverallQual'], train['SalePrice'])
plt.show()

fig = plt.figure(constrained_layout=True, figsize=(8,5))
sns.scatterplot(train['GrLivArea'], train['SalePrice'])
plt.show()

#form above plots we can see 'GrLivArea' and 'SalePrice' have good relation
#there are few outliers
#for now we will keep outliers,we will figure out it later
##plot fig sizing
import matplotlib.style as style
style.use('ggplot')
sns.set_style('whitegrid')
plt.subplots(figsize = (30,20))
##plotting heatmap

#generate a mask for the upper triangel (taken from seaborn example gallery)
mask = np.zeros_like(train.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

sns.heatmap(train.corr(), cmap=sns.diverging_palette(20, 220, n=200), mask =mask, annot=True, center = 0, );
##give title
plt.title("Heatmap of all the Features", fontsize = 30);
plt.show()

#we can see there is multicollinearity between some features
#this can figure it later

#now we are done with most of the Feature analysis,let's beging with the feature engineering
#again concat train and test cause we have done changes in train dataset
data = pd.concat((train,test)).reset_index(drop=True)

#check values in each column
columns = data.columns

for col in columns:
    print(data[col].value_counts())
    print('\n')

#now check missing values
missing_tot = data.isnull().sum().sort_values(ascending = False)
missing_per = ((data.isnull().sum()/data.isnull().count())*100).sort_values(ascending = False)
missing_data = pd.concat([missing_tot, missing_per] , axis=1, keys=['Total', 'Percent'])
missing_data.head(40)

#now separate the catgorical freatures and numerical features
data_cat = data.select_dtypes('object')
data_int = data.select_dtypes(['int64','float64'])

data_cat.columns
data_cat,isnull().sum().sort_values(ascending = False)
d = data_cat,isnull().sum().sort_values(ascending = False)
d.index


#to decide about null values I have done old type analysis by using paper and pen
#for example, Like in 'PoolQc' column 2908 null values,but in as per data description PoolQc: Pool quality

#means null values are representing no pool so fill them by 'none'
#one more example, if'GarageType' is null and as per data description

#means null values neans no Garage so fill them by 'none'
#and the features related to Garage like 'GarageYrBit','GarageFinish','GarageCars', will follow same lead
#like in('GarageCars':Size of garage in car capacity) if there is now Garage means 'GarageCars' null represents 'O'
#as we can see 'GarageCars' column in above value count code

#use data description for fill null values
#fill null values by none cause this null represpents they are not available on site so fill by 'none'
columns1 = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu']








