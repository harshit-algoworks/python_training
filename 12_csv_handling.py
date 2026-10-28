import pandas as pd

df = pd.read_csv(r"C:\Users\HarshitArora\Desktop\python\BigMart_Sales.csv") # read the csv file and store it in a dataframe
# print(df) # prints the dataframe

# df2 = [12,32,43,54,65,76,87,98,109,120]
# df2 = pd.Series(df2, index = ['01','02','03','04','05','06','07','08','09','10']) # convert the list to a series
# print(df2) # prints the series


dairy = df[df['Item_Type'] == 'Dairy']
sales = df['Item_Outlet_Sales'].sum()
sales_by_type = df.groupby('Item_Type')['Item_Outlet_Sales'].sum()
# print(sales) # prints the sum of the sales of all the items in the dataframe
print(sales_by_type) # prints the sum of the sales of each item type in the dataframe