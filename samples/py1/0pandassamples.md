# Expressions and Lazy Conjecture   

## Set value based on filtered match
expressions.loc[(expressions["operator"] == ">") & (expressions['left_value'] > expressions['right_value']), 'value'] = "true"

## filter lambda by each row
df.apply(lambda row: row['A'] > 10, axis=1): This applies the lambda function to each row, checking if the value in column A is greater than 10.
df[...]: This filters the DataFrame based on the boolean Series returned by the apply method.
filtered_df = df[df.apply(lambda row: row['A'] > 10, axis=1)]

## Join the Party
pd.merge(df1,df2, on=join_col, how)

## Union
pd.concat([df1,df2], axis=ifnotdefault)

## Campfire cause.. group

    enrollments_grade=enrollments.groupby("student_id")["grade"].max().reset_index()


## Sample Where do we go
scores['points'] = np.where(
        scores['goals_for'] > scores['goals_against'], 
        3, 
        np.where(scores['goals_for'] == scores['goals_against'], 1, 0)
    )
## Pandas hugs