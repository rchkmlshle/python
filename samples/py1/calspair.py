import pandas as pd
""""
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
"""
def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:
    calls['person1']   = calls[['from_id', 'to_id' ]].min(axis=1) #sql least, greatest
    calls['person2']  =calls[['from_id','to_id']].max(axis=1)
    return calls.groupby(['person1', 'person2']).agg(call_count=('duration', 'count'
                                                                 ),total_duration=('duration', 'sum'
                                                                                   )).reset_index()