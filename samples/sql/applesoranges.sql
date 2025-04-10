-- Write your PostgreSQL query statement below
------
select 
    sale_date, 
    sum(sold_num) filter (where fruit = 'apples') - sum(sold_num) filter (where fruit = 'oranges') as diff
from 
    sales
group by 1
order by 1;
--filter clause
-------------------
with apples as
(
select sale_date, fruit, sum(sold_num) as soldnum
from sales
where fruit='apples'
group by sale_date, fruit
),
oranges as
(
select sale_date, fruit, sum(sold_num) soldnum
from sales
where fruit='oranges'
group by sale_date, fruit) 
select apples.sale_date, (apples.soldnum - oranges.soldnum) as diff
from apples, oranges
where apples.sale_date=oranges.sale_date

---- cross join, will fail for multiple fruit, speed, less valid.
select s.sale_date, 
s.sold_num - t.sold_num as diff


from Sales s join Sales t 
on s.sale_date = t.sale_date 
and s.fruit != t.fruit
where s.fruit='apples'
order by 1