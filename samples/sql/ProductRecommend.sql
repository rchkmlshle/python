/*

Companies
SQL Schema
Pandas Schema
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

The result format is in the following example.\
*/
-----
-- Write your PostgreSQL query statement below
WITH cte1 AS (SELECT customer_id, ARRAY_AGG(product_name) AS agg
FROM Orders
GROUP BY customer_id)

SELECT customer_id, customer_name
FROM Customers 
WHERE customer_id IN (SELECT customer_id 
                        FROM cte1
                        WHERE 'A'= ANY(agg) AND 'B'= ANY(agg) AND NOT('C' = ANY(agg))
                        )
/*cte table ARRAY_AGG
| customer_id | agg     |
| ----------- | ------- |
| 3           | A,B,D   |
| 4           | C       |
| 2           | A       |
| 1           | A,B,D,C |
*/

---
SELECT customer_id, customer_name
FROM
    Customers
    LEFT JOIN Orders USING (customer_id)
GROUP BY 1
HAVING SUM(product_name = 'A') > 0 AND SUM(product_name = 'B') > 0 AND SUM(product_name = 'C') = 0
ORDER BY 1;

----

