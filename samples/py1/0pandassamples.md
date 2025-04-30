# Expressions 

## Pivot
    df= sales.pivot(index='sale_date',columns='fruit',values='sold_num').reset_index()


## Set value based on filtered match
expressions.loc[(expressions["operator"] == ">") & (expressions['left_value'] > expressions['right_value']), 'value'] = "true"

## filter lambda by each row
df.apply(lambda row: row['A'] > 10, axis=1): This applies the lambda function to each row, checking if the value in column A is greater than 10.
df[...]: This filters the DataFrame based on the boolean Series returned by the apply method.
filtered_df = df[df.apply(lambda row: row['A'] > 10, axis=1)]

## Join the Party
pd.merge(df1,df2, on=join_col, how)

## Union.. Imagine 
pd.concat([df1,df2], axis=ifnotdefault)

## Campfire cause.. group

    enrollments_grade=enrollments.groupby("student_id")["grade"].max().reset_index()


## Sample Where do we go
scores['points'] = np.where(
        scores['goals_for'] > scores['goals_against'], 
        3, 
        np.where(scores['goals_for'] == scores['goals_against'], 1, 0)
    )
## Pandas 
Ailuropoda melanoleuca eq “black and white cat-foot”.

## lambdas , list comprehensions
[(lambda x: x ** 2)(num) for num in numbers]
[f(x) for x in xs if x is not None else '']

sort counters, dicts, returns list of lists
sorted_num=sorted(count.items(), key=lambda x:(x[1],-x[0]))