# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 01:37:46 2022

@author: Facu
"""

import pandas as pd

data = pd.read_csv('transaction.csv', sep=';')
data.info()

#Defining variables
CostPerItem = data['CostPerItem']
SellingPricePerItem = data['SellingPricePerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']

#Mathematical operations on tableau
ProfitPerItem = SellingPricePerItem - CostPerItem
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#Adding new column to data frame
data['CostPerTransaction'] = CostPerTransaction
data['SalesPerTransaction'] = NumberOfItemsPurchased * SellingPricePerItem

#Profit calculation
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup calculation
data['Markup'] = round((data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction'], 2)

#Formating date field
day = data['Day'].astype(str)
month = data['Month'].astype(str)
year = data['Year'].astype(str)
MyDate = day + '-' + month + '-' + year

data['Date'] = MyDate

#Separating ClientKeywords column
SplitCol = data['ClientKeywords'].str.split(',', expand=True)

#Creating new columns from the splited column
data['ClientAge'] = SplitCol[0]
data['ClientType'] = SplitCol[1]
data['LengthOfContract'] = SplitCol[2]

#Replacing '[' and ']' with nothing
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

#Using lowercase function on ItemDescription column
data['ItemDescription'] = data['ItemDescription'].str.lower()

#Merging files
#Bringing in a new dataset
dataSeasons = pd.read_csv('value_inc_seasons.csv', sep=';')

data = pd.merge(data, dataSeasons, on = 'Month')

#Dropping columns
data = data.drop(['Day', 'Month', 'Year', 'ClientKeywords'], axis = 1)

#Exporing DF into CSV
data.to_csv('ValueInc_Cleaned.csv', index = False)
















