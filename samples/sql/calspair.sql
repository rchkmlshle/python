-- Write your PostgreSQL query statement below
/*
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| from_id     | int     |
| to_id       | int     |
| duration    | int     |
+-------------+---------+
This table does not have a primary key (column with unique values), it may contain duplicates.
This table contains the duration of a phone call between from_id and to_id.
from_id != to_id
 Write a solution to report the number of calls and the total call duration between
  each pair of distinct persons (person1, person2) where person1 < person2.
*/

---no cte, subquery
select
    least(from_id, to_id) person1, 
    greatest(from_id, to_id) person2, 
    count(*) call_count,
    sum(duration) total_duration
from calls
group by 1, 2


--------
with cte as (
select
case when from_id< to_id then from_id else to_id end as person1,
case when from_id > to_id then from_id else to_id end as person2,
duration from calls
)
select person1, person2,
count(*) as call_count,
sum(duration) as total_duration
from cte
group by person1, person2
--having(from_id<to_id)
order by  person1, person2