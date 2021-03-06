# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data_df = pd.DataFrame(purchase_data)
purchase_data_df.head()

total_players = purchase_data_df["SN"].count()
total_players

unique_items = len(purchase_data_df["Item ID"].unique())
unique_items

total_purchases = purchase_data_df["Purchase ID"].count()
total_purchases

total_revenue = purchase_data_df["Price"].sum()
total_revenue

average_price1 = purchase_data_df["Price"].mean()
average_price1

average_price2 = total_revenue/total_purchases
average_price2

# average_price1 = average_price2

# Display the summary data frame
purchase_analysis_df = pd.DataFrame([{"Number of Unique Items": unique_items, "Average Price": average_price1,
                                      "Number of Purchases": total_purchases, "Total Revenue": total_revenue}])
purchase_analysis_df["Average Price"] = purchase_analysis_df["Average Price"].map("${:,.2f}".format)
purchase_analysis_df["Total Revenue"] = purchase_analysis_df["Total Revenue"].map("${:,.2f}".format)
purchase_analysis_df

# The value counts method counts unique values in a column, then dataframe created to hold results
gender_demo_df = pd.DataFrame(purchase_data_df["Gender"].value_counts())
gender_demo_df

percentage_of_players = (purchase_data_df["Gender"].value_counts()/total_players)*100
percentage_of_players

# Calculations performed and added into Data Frame as a new column
gender_demo_df["Percentage of Players"] = percentage_of_players
gender_demo_df["Percentage of Players"] = gender_demo_df["Percentage of Players"].map("{:,.2f}%".format)
gender_demo_df

# Using GroupBy in order to separate the data into fields according to "Gender" values
gender_grouped_purchased_data_df = purchase_data_df.groupby(["Gender"])

# The object returned is a "GroupBy" object and cannot be viewed normally...
# print(gender_grouped_purchased_data_df)

# In order to be visualized, a data function must be used...
gender_grouped_purchased_data_df["Purchase ID"].count().head(10)

# Get total purchase value by gender
total_purchase_value = gender_grouped_purchased_data_df["Price"].sum()
total_purchase_value.head()
dlr_total_purchase_value = total_purchase_value.map("${:,.2f}".format)
dlr_total_purchase_value.head()

# Average purchase price by gender
avg_purchase_price = gender_grouped_purchased_data_df["Price"].mean()
avg_purchase_price.head()
dlr_avg_purchase_price = avg_purchase_price.map("${:,.2f}".format)
dlr_avg_purchase_price.head()

# Normalized totals, total purchase value divided by purchase count by gender
normalized_totals = total_purchase_value/gender_grouped_purchased_data_df["Purchase ID"].count()
dlr_normalized_totals = normalized_totals.map("${:,.2f}".format)
dlr_normalized_totals.head()

# Organize summary gender data, get all columns to organized Data Frame, add needed columns to it
org_gender_purchased_data_df = pd.DataFrame(gender_grouped_purchased_data_df["Purchase ID"].count())
org_gender_purchased_data_df["Average Purchase Price"] = dlr_avg_purchase_price  
org_gender_purchased_data_df["Total Purchase Value"] = dlr_total_purchase_value 
org_gender_purchased_data_df["Normalized Totals"] = dlr_normalized_totals 
org_gender_purchased_data_df

# Summary purchasing analysis DF grouped by gender, rename "Purchase ID" column, using .rename(columns={})
summary_gender_purchased_data_df = org_gender_purchased_data_df.rename(columns={"Purchase ID":"Purchase Count"})
summary_gender_purchased_data_df


# Create new data frame with items related information 
items = purchase_data[["Item ID", "Item Name", "Price"]]

# Group the item data by item id and item name 
item_stats = items.groupby(["Item ID","Item Name"])

# Count the number of times an item has been purchased 
purchase_count_item = item_stats["Price"].count()

# Calcualte the purchase value per item 
purchase_value = (item_stats["Price"].sum()) 

# Find individual item price
item_price = purchase_value/purchase_count_item

# Create data frame with obtained values
most_popular_items = pd.DataFrame({"Purchase Count": purchase_count_item, 
                                   "Item Price": item_price,
                                   "Total Purchase Value":purchase_value})

# Sort in descending order to obtain top spender names and provide top 5 item names
popular_formatted = most_popular_items.sort_values(["Purchase Count"], ascending=False).head()

# Format with currency style
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})