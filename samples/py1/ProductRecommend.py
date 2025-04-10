"""

Companies
Table: Customers

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| customer_id         | int     |
| customer_name       | varchar |
+---------------------+---------+
customer_id is the column with unique values for this table.
customer_name is the name of the customer.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| product_name  | varchar |
+---------------+---------+
order_id is the column with unique values for this table.
customer_id is the id of the customer who bought the product "product_name".
 

Write a solution to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product "C" since we want to recommend them to purchase this product.

Return the result table ordered by customer_id.

The result format is in the following example.
"""

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust_prods=orders.pivot(index="customer_id", 
                            columns='product_name', values="order_id")
    cust_name_prods=pd.merge(
        customers, cust_prods,
        on="customer_id",
        how="left join"
    )

    cust_name_prods_rec=cust_name_prods[cust_name_prods.apply(
        lambda row: pd.notnull(row["A"]) & pd.notnull(row["B"]) & pd.isnull(row["C"]),
        axis=1)].reset_index(drop=True)
    return cust_name_prods_rec[["customer_id", "customer_name"]]
