# Samples
## moving aggregation
    select *, sum(weight) over 
        (order by turn 
        rows between unbounded preceding and current row) as total
        from queue 

## partioned average/calculation 
    select 
    distinct 
    student_id, 
    first_value(course_id)over(partition by student_id order by grade desc, course_id)  as course_id,
    first_value(grade)over(partition by student_id order by grade desc) as grade
    from Enrollments a
    order by 1

## Aggregated Filter
    SELECT customer_id, customer_name
    FROM
        Customers
        LEFT JOIN Orders USING (customer_id)
    GROUP BY 1
    HAVING SUM(product_name = 'A') > 0 AND SUM(product_name = 'B') > 0 AND SUM(product_name = 'C') = 0
    ORDER BY 1;