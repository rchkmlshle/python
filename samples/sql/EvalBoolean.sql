/*
Table Variables:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| name          | varchar |
| value         | int     |
+---------------+---------+
In SQL, name is the primary key for this table.
This table contains the stored variables and their values.
 

Table Expressions:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| left_operand  | varchar |
| operator      | enum    |
| right_operand | varchar |
+---------------+---------+
In SQL, (left_operand, operator, right_operand) is the primary key for this table.
This table contains a boolean expression that should be evaluated.
operator is an enum that takes one of the values ('<', '>', '=')
The values of left_operand and right_operand are guaranteed to be in the Variables table.
 

Evaluate the boolean expressions in Expressions table.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Variables table:
+------+-------+
| name | value |
+------+-------+
| x    | 66    |
| y    | 77    |
+------+-------+
Expressions table:
+--------------+----------+---------------+
| left_operand | operator | right_operand |
+--------------+----------+---------------+
| x            | >        | y             |
| x            | <        | y             |
| x            | =        | y             |
| y            | >        | x             |
| y            | <        | x             |
| x            | =        | x             |
+--------------+----------+---------------+
Output: 
+--------------+----------+---------------+-------+
| left_operand | operator | right_operand | value |
+--------------+----------+---------------+-------+
| x            | >        | y             | false |
| x            | <        | y             | true  |
| x            | =        | y             | false |
| y            | >        | x             | true  |
| y            | <        | x             | false |
| x            | =        | x             | true  |
+--------------+----------+---------------+-------+
Explanation: 
As shown, you need to find the value of each boolean expression in the table using the variables table.
*/
---------------
select team_id, team_name, 
sum(case when team_id=m.host_team and m.host_goals>m.guest_goals then 3 
         when team_id=m.host_team and m.host_goals=m.guest_goals then 1 
         when team_id=m.guest_team and m.host_goals<m.guest_goals then 3 
         when team_id=m.guest_team and m.host_goals=m.guest_goals then 1 
         else 0 end) as num_points
from teams t, matches m
group by team_id, team_name
order by num_points DESC, team_id
-----multiple case, join on two cols

-- Write your PostgreSQL query statement below
select e.left_operand, e.operator, e.right_operand,
       case 
       when e.operator = '<' then 
         case when l.value < r.value then 'true' else 'false' end
       when e.operator = '>' then 
           case when l.value > r.value then  'true' else  'false' end
       else 
        case when l.value = r.value then 'true' else 'false' end
       end
       as value
from Expressions e
join Variables l
on e.left_operand = l.name
join Variables r
on e.right_operand = r.name


