import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


#Importing data and performing initial analysis
data = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
print(data.order_amount.describe())
data.boxplot(column = "order_amount")
plt.title("Dataset boxplot",fontsize=18)
plt.text(300, 87, "Data contains outliers",fontsize=12 )
plt.ylabel("Order values",fontsize=14)
plt.show()


# Visualizing 90 most frequent order values
value_index = data.order_amount.value_counts()
value_index = value_index[0:90]
median = data.order_amount.median()
plt.stem(value_index.index,value_index.values) 
plt.axvline(median,color="r", linestyle="--")
plt.xticks(np.arange(min(value_index.index), max(value_index.index)+1, 25.0))
plt.text(300, 87, "Median :" + str(median),fontsize=14 )
plt.title("Occurence of 90 most frequent order values",fontsize=18)
plt.xlabel("Order value",fontsize=14)
plt.ylabel("Occurence of orders",fontsize=14)
plt.grid(axis='y')
plt.show()

# Dictionary with total dollar amount per shop
shop_order_dict = {}

for i in range (data.order_amount.size):
    if data.shop_id[i] in shop_order_dict.keys():
        shop_order_dict[data.shop_id[i]] += data.order_amount[i]
    else:
        shop_order_dict[data.shop_id[i]] = data.order_amount[i]

#Visualizing total order dollar amount per shop
order_volume = list(shop_order_dict.values())
plt.stem(shop_order_dict.keys(),np.log(order_volume)) 
plt.title("Shops by dollar amount",fontsize=18)
plt.xlabel("Shop ID",fontsize=14)
plt.ylabel("Sales volume (in logarithmic scale)",fontsize=14)
plt.grid(axis='y')
plt.xticks(np.arange(min(shop_order_dict.keys())+1, max(shop_order_dict.keys())+1, 2.0))
plt.show()

#Determining the impact on the dataset of orders above $2000
expensive_orders = data.order_amount[data.order_amount >= 2000]
print("Dolar value ratio of orders above $2000 with respect to all orders: " + str(np.sum(expensive_orders)/np.sum(data.order_amount)*100))
print("Ratio of number of orders above $2000 with respect to all orders: " + str(np.size(expensive_orders)/np.size(data.order_amount)*100))


