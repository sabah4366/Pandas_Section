import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style 
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
# print(datas.isnull().sum())

#5-values_count() will give you the values in the column we used
# print(datas['Customer Name'].value_counts())

#6-give you the sum of the null values  in each clumn
# print(datas.isna().sum())

# 7-will delete entire the row if anyone is null value
# datas.dropna(inplace=True)

#8- you cn change the datatype of column 
# datas['ID'] = datas['ID'].astype('int')

#9- it will give you the values in that cloumn and their count
# print(datas.value_counts('Order Priority'))

#10-I WANT TO CLEAN DATA USING THE SIZE COLUMN BCS SIZE COLUMN HAS KB AND MB SO I WANT TO CONVERT THAT INTO MB
#is there any value u want to convert into nan use -> return numpy.nan
# def convert_data_type_size(rec):
#     if 'M' in rec:
#         rec = rec.replace('M','')
#         return  float(rec)
#     elif 'K' in rec:
#         rec = rec.replace('K','')
#         return float(rec)/1024
#     else:
#         return float(rec)
# datas['Size'] = datas['Size'].map(convert_data_type_size)
# mean = datas['Size'].mean()

#11-can fill with null value in size clumn with mean
# datas['Size'].fillna(mean,inplace=True)

#12 head() will give u the starting five reports. if you want starting 10 reports use 10 inside of head(10)
# print(datas.head(10))

#13 you can directly replace from the cloumn values using str if value is in string 
#in this Product Container cloumn values seperated with space i replaced that with minus (-)
# datas['Product Container'] = datas['Product Container'].str.replace(' ', '-')
# print(datas.info())

#14 Matplot lib
x=[1,10,4,3,8,5,9,2,7,6]
y=[1000,1200,200,2000,600,800,1400,1600,1800,400]

colors = ['red', 'green', 'blue','yellow','black','orange','violet','grey','purple','pink']
# plt.bar(x,y,color=colors)
# plt.title("BAR CHART")
# plt.xlabel("X Axis")
# plt.ylabel('Y Axis')
# plt.show()


#14 pie plot using matplotlib
#pieplot is categorical versus numerical
#pie plot calculation for each slices is number divide by total *360 
#eg:[10,30,50,70] -> 10+30+50+70 = 160 so the slice space of 10 in piechart has (10 / 160) * 360 -> that 360 is total degree of pie
#if you want the percentage in  pie u can pass autopct="%2.if%%" in pie
#autopct is basically used to display the percentage value using string formatting and it will add percentage in our slices or wedges
# y = np.array([100,23,59,145])
# x = np.array(['India','Germany',"China",'America'])
# plt.pie(y,labels=x,autopct="%12.0f%%")
# plt.show()

#that method is for return the actual amount instead of percentage in slices
cost_x = ['Bullet','Himalaya','Pulsar','Access','Activa','Splender']
bike_y = [230000,400000,190000,80000,90000,145000] 
# def show_amount(pct,cost_x):
#     absolute = (pct / 100. * sum(cost_x))
#     return f"{round(absolute)} OMR" 
#explode will make cut out of the pie 0 means nothing o.2 or any will goes to outside
explodes = []
#this method is for largest value of slice i want make it cut out from the pie
# max_value = max(cost_x)
# for cost in cost_x:
#     if cost == max_value:
#         explodes.append(0.2)
#     else:
#         explodes.append(0)

plt.pie(cost_x,labels=bike_y)   
# plt.pie(cost_x,labels=bike_y,autopct=lambda pct : show_amount(pct,cost_x))
plt.show()

