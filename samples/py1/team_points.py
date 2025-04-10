"""

Companies
SQL Schema
Pandas Schema
Table: Teams

+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| team_id       | int      |
| team_name     | varchar  |
+---------------+----------+
team_id is the column with unique values of this table.
Each row of this table represents a single football team.
 

Table: Matches

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| host_team     | int     |
| guest_team    | int     | 
| host_goals    | int     |
| guest_goals   | int     |
+---------------+---------+
match_id is the column of unique values of this table.
Each row is a record of a finished match between two different teams. 
Teams host_team and guest_team are represented by their IDs in the Teams table (team_id), and they scored host_goals and guest_goals goals, respectively.
 

You would like to compute the scores of all teams after all matches. Points are awarded as follows:
A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).
Write a solution that selects the team_id, team_name and num_points of each team in the tournament after all described matches.

Return the result table ordered by num_points in decreasing order. In case of a tie, order the records by team_id in increasing order.

The result format is in the following example.
"""

import pandas as pd
import numpy as np

def team_scores(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    hosts = (
        matches[['host_team', 'host_goals', 'guest_goals']]
        .rename(columns={'host_team': 'team_id', 'host_goals': 'goals_for', 'guest_goals': 'goals_against'})
    )
    guests = (
        matches[['guest_team', 'guest_goals', 'host_goals']]
        .rename(columns={'guest_team': 'team_id', 'guest_goals': 'goals_for', 'host_goals': 'goals_against'})
    )
    scores = pd.concat([hosts, guests])
    scores['points'] = np.where(
        scores['goals_for'] > scores['goals_against'], 
        3, 
        np.where(scores['goals_for'] == scores['goals_against'], 1, 0)
    )

    result = (
        pd.merge(teams, scores, how='left', on='team_id')
        .groupby(['team_id', 'team_name'])
        .agg(num_points=('points', 'sum'))
        .reset_index()
        .sort_values(['num_points', 'team_id'], ascending=[False, True])
    )

    return result
