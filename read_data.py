import pandas as pd

df = pd.read_csv("premier-league-matches.csv")

# shape:
#  (12026, 8)
print(f"shape:\n", df.shape)

# head:
#     Season_End_Year  Wk  ...            Away FTR
# 0             1993   1  ...   Middlesbrough   H
# 1             1993   1  ...       Wimbledon   H
# 2             1993   1  ...  Manchester Utd   H
# 3             1993   1  ...       Blackburn   D
# 4             1993   1  ...    Norwich City   A
# [5 rows x 8 columns]
print(f"head:\n", df.head())

# data types:
#  Season_End_Year     int64
# Wk                  int64
# Date               object
# Home               object
# HomeGoals           int64
# AwayGoals           int64
# Away               object
# FTR                object
# dtype: object
print(f"data types:\n", df.dtypes)

# nulls:
#         Season_End_Year     Wk   Date  ...  AwayGoals   Away    FTR
# 0                False  False  False  ...      False  False  False
# 1                False  False  False  ...      False  False  False
# 2                False  False  False  ...      False  False  False
# 3                False  False  False  ...      False  False  False
# 4                False  False  False  ...      False  False  False
# ...                ...    ...    ...  ...        ...    ...    ...
# 12021            False  False  False  ...      False  False  False
# 12022            False  False  False  ...      False  False  False
# 12023            False  False  False  ...      False  False  False
# 12024            False  False  False  ...      False  False  False
# 12025            False  False  False  ...      False  False  False
# [12026 rows x 8 columns]
print(f"nulls:\n", df.isnull())

# count nulls:
#  Season_End_Year    0
# Wk                 0
# Date               0
# Home               0
# HomeGoals          0
# AwayGoals          0
# Away               0
# FTR                0
# dtype: int64
print(f"count nulls:\n", df.isnull().sum())