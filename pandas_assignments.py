import pandas as pd
import numpy as np
#1
datas = pd.read_excel('copydata.xlsx')
#print(datas.shape)
#will get the unit price > 34 
#print(datas[datas['Unit Price']>34])
#it will replace index with Order Priority column permanently thats why
# inplace=True if we not put inplace=True it will temporarly only show the index as Order Priority
# datas.set_index('Order Priority',inplace=True)
#it will show the index with Medium
# print(datas.loc["Medium"])
# datas.reset_index()

#2
# converters if the column has any null values 
# you can also add multiple funmction for each column
# def convert_column_unit_prise(col):
#     print('col',col)
#     if not col:
#         return 'Not Values Here'
#     else:
#         return col
# datas = pd.read_excel('copydata.xlsx',converters={
#     'Customer Name':convert_column_unit_prise,
#     'Unit Price':convert_column_unit_prise,
#     'Discount':convert_column_unit_prise,
#     'Row ID':convert_column_unit_prise,

# })
# print(datas)

#3-if you want to delete a complete row you can use drop 
#axis =1 -> column
#axis = 0 -> row
# print(datas.info())
# print(datas.drop("ID",axis=1,inplace=True))
# print(datas)

#4-show th sum of null values for each column
print(datas.isnull())

#5-values_count() will give you the values in the column we used
# print(datas['Customer Name'].value_counts())
print('---------------------------------------------------')
#6-give you the sum of the null values  in each clumn
print(datas.isna())

# 7-will delete entire the row if anyone is null value
# datas.dropna(inplace=True)

#8- you cn change the datatype of column 
# datas['ID'] = datas['ID'].astype('int')

#9- 