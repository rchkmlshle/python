"""
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
-- layered cte, global avg by partition query"
"""

import pandas as pd

def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    
    import pandas as pd

def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    calls_x = calls.drop(columns=["callee_id"], axis=1).rename(columns={"caller_id":"id"})
    calls_y=calls.drop(columns=["caller_id"], axis=1).rename(columns={"callee_id":"id"})

    calls_new=pd.concat([calls_x, calls_y]) #union

    global_avg=calls_new["duration"].mean() #full col mean

    country_new =country.rename(columns={"name":"country"})
    person["country_code"]=person["phone_number"].str[:3]
    merged_country_person=pd.merge( person, country_new, on="country_code", how="left")
    merged_country_person_calls=pd.merge(merged_country_person, calls_new, on="id", how="left")
    avg_by_country=merged_country_person_calls.groupby(["country"], as_index=False)["duration"].mean()
    #return group by as df , new column
    df=avg_by_country[avg_by_country["duration"]> global_avg][["country"]]
    return df

    