# This code module focuses on cleaning up the data.
# It will attmpt to remove null values, reduce the number of columns, and structure the data for data analysis


import pandas as pd
from sodapy import Socrata
import numpy as np


def clean_data():  
#The following lines of code extract the data set from the web using Socrata and endpoints without API.
   iowa_data = Socrata("mydata.iowa.gov", None)

   iowa_file= iowa_data.get("m3tr-qhgy", limit=100)

#Here we create a data frame using pandas
   iowa_file_df = pd.DataFrame.from_records(iowa_file)

#In this create a subset of the data that includes the neccesary columns.
   iowa_file_subset_df = iowa_file_df[["state_bottle_cost","state_bottle_retail","sale_bottles","category_name","county","address","zipcode"]]
 
# This lines of code turn the both state_bottle_cost, state_bottle_retail, and sale_bottles converts any empty spaces to zeros in the whole dataframe
   iowa_file_subset_df = iowa_file_subset_df.replace('', 0)

#This code turn the numeric columns to float to be able to perform statistic analysis later
   iowa_file_subset_df["state_bottle_cost"] = iowa_file_subset_df.state_bottle_cost.astype(float)
   iowa_file_subset_df["state_bottle_retail"] = iowa_file_subset_df.state_bottle_retail.astype(float)
   iowa_file_subset_df["sale_bottles"] = iowa_file_subset_df.sale_bottles.astype(float)

# This line of code eliminates any zeros in our numeric columns
   iowa_file_subset_df  = iowa_file_subset_df[(iowa_file_subset_df['state_bottle_cost'] > 0) & (iowa_file_subset_df['state_bottle_cost'] > 0) & (iowa_file_subset_df["sale_bottles"])]

# This creates a dataframe column called profit from substracting both the bottle price and cost columns
   iowa_file_subset_df["profit"] = iowa_file_subset_df.state_bottle_retail - iowa_file_subset_df.state_bottle_cost

# This creates a dataframe column called total profit by multiplying profit per units times total bottles sold
   iowa_file_subset_df["total_profit"] = iowa_file_subset_df.profit * iowa_file_subset_df.sale_bottles

# This restructure the order of the columns
   sequence = ["state_bottle_cost","state_bottle_retail","sale_bottles","profit","total_profit","category_name","county","address","zipcode"]
   iowa_file_subset_df = iowa_file_subset_df.reindex(columns=sequence)

#This line of code rounds total profit column to 1 decimal point 
   iowa_file_subset_df["total_profit"] = round(iowa_file_subset_df["total_profit"],1)
   iowa_file_subset_df = iowa_file_subset_df.rename(columns={"state_bottle_cost":"Bottle_Cost","state_bottle_retail":"Bottle_Selling_Price","sale_bottles":"Bottle_Quantity_Sold",
                                                          "profit":"Profit",
                                                          "total_profit":"Total_Profit",
                                                          "category_name":"Bottle_Category_Name", "county":"County","address":"Client_Store_Address","zipcode":"Zipcode"})
   
   return iowa_file_subset_df

  

   
