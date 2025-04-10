-- Write your PostgreSQL query statement below

/*
Table Person:

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| name           | varchar |
| phone_number   | varchar |
+----------------+---------+
id is the column of unique values for this table.
Each row of this table contains the name of a person and their phone number.
Phone number will be in the form 'xxx-yyyyyyy' where xxx is the country code (3 characters) and yyyyyyy is the phone number (7 characters) where x and y are digits. Both can contain leading zeros.
 

Table Country:

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| name           | varchar |
| country_code   | varchar |
+----------------+---------+
country_code is the column of unique values for this table.
Each row of this table contains the country name and its code. country_code will be in the form 'xxx' where x is digits.
 

Table Calls:

+-------------+------+
| Column Name | Type |
+-------------+------+
| caller_id   | int  |
| callee_id   | int  |
| duration    | int  |
+-------------+------+
This table may contain duplicate rows.
Each row of this table contains the caller id, callee id and the duration of the call in minutes. caller_id != callee_id
 

A telecommunications company wants to invest in new countries. The company intends to invest in the countries where the average call duration of the calls in this country is strictly greater than the global average call duration.

Write a solution to find the countries where this company can invest.

Return the result table in any order.

The result format is in the following example.

*/

-- Write your PostgreSQL query statement below
-- layered cte, global avg by partition query
WITH cte_calls AS 
(
    --caller
    SELECT  LEFT(p.phone_number, 3) AS country_id,
            duration
    FROM    Calls AS c
        LEFT JOIN Person AS p
            ON c.caller_id = p.id --caller

    UNION ALL

    --callee
    SELECT  LEFT(p.phone_number, 3) AS country_id,
            duration
    FROM    Calls AS c
        LEFT JOIN Person AS p
            ON c.callee_id = p.id --callee

),

cte AS (
    SELECT  country_id,
            c.name AS country,
            AVG(duration) OVER(PARTITION BY country_id) AS country_avg,
            AVG(duration) OVER() AS global_avg  
    FROM    cte_calls AS calls
        LEFT JOIN Country AS c
            ON calls.country_id = c.country_code
)

SELECT  DISTINCT country
FROM    cte
WHERE   country_avg > global_avg


-----
with 
global_avg as
(
    select avg(duration ) as global_avg
    from calls 
    ),
calls_country as --country person xref
(
    select person.id as person_id, country.name as country
    from person, country
    where substring(phone_number, 1, 3) = country.country_code
),
duration_person as --- pivot person
(
   select caller_id as person_id, duration from calls
   union all
   select callee_id as person_id, duration from calls
)
select country
from  calls_country, duration_person
where calls_country.person_id=duration_person.person_id
group by country
having avg(duration) > (select global_avg from global_avg limit 1)

