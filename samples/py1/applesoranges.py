import pandas as pd
"""
how many more apples sold than oranges.. welcome to new age AI space age of RIP soon IT
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| sale_date     | date    |
| fruit         | enum    | 
| sold_num      | int     | 
+---------------+---------+
"""
def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    df= sales.pivot(index='sale_date',columns='fruit',values='sold_num').reset_index()
    """
    fruit   sale_date  apples  oranges
        0      2020-05-01      55       75
        1      2020-05-07      55       45
    """
    df['diff']= df['apples']-df['oranges']
    return df.sort_values(by='sale_date')[['sale_date','diff']]

def main():
    df=pd.DataFrame(
        [{ "sale_date" : "2020-05-01", "fruit": "apples", "sold_num":55},
         {"sale_date" : "2020-05-01", "fruit": "oranges", "sold_num":75},
         {"sale_date" : "2020-05-07", "fruit": "apples", "sold_num":55},
          {"sale_date" : "2020-05-07", "fruit": "oranges", "sold_num":45}
        ]
    )

    apples_oranges(df)

if __name__=='__main__':
    main()