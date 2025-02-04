 /*
 +-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id column contains unique values.
This table has the information about all people waiting for a bus.
The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board.
weight is the weight of the person in kilograms.
*/

--Solution1
 select person_name 
 from
 (
    select person_name,
    sum(weight) over (order by turn) as total_weight
    from queue
 ) as wq
 where total_weight<=1000
 order by total_weight DESC
 LIMIT 1

 ---Solution 2. Mars super duper Genius complex version
 with cta 
as
(
    select *, sum(weight) over 
    (order by turn 
    rows between unbounded preceding and current row) as total
    from queue 
)
select person_name 
from cta
where total<=1000
order by total desc
limit 1