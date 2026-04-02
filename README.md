# premier_league_outcome_ml
Predicting the outcomes of premier league games

## Problem Definition:
### What type of problem?
Classification problem, predicting the outcome of a premier league game--win, loss, tie

## Data Source:
Kaggle Premier League Dataset (1993-2023):
https://www.kaggle.com/datasets/evangower/premier-league-matches-19922022

### Features:
Season_End_Year
Wk
Date
Home
HomeGoals
AwayGoals
Away
FTR (Full Time Result)

## Examining the data
### Class imbalance check:
None--distribution (45% home win, 28% away win, 25% draw)

### Model decision:
Classification problem -> Logistic Regression Model

## Training
Sklearn

## Testing
Using classification_report:
-> heavy bias towards predicting Home Win

## What I Learned:
How to start a ml project, how to find data, how to train a model, how to determine if a model is good (while being aware of class imbalance)

## Next Steps:
Train my tennis model!