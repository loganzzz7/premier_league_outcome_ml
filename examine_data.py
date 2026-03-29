import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('premier-league-matches.csv')

# first decode FTR--full time result to more readable terms
df['result'] = df['FTR'].map({'H':'Home Win', 'A':'Away Win', 'D':'Draw'})

# Counts of unique vals:
#  result
# Home Win    5519
# Away Win    3410
# Draw        3097
# Name: count, dtype: int64
print(f"Counts of unique vals:\n", df['result'].value_counts())

# Counts of unique vals (percentages):
#  result
# Home Win    0.459
# Away Win    0.284
# Draw        0.258
# Name: proportion, dtype: float64
print(f"Counts of unique vals (percentages):\n", df['result'].value_counts(normalize=True).round(3))

# need to do this to avoid class imbalance
# we can see that not one result is overly dominant -> won't lead to erronous prediction
# e.g. defaulting to predicting homewin if homewin is 75% and achieving 75% accuracy

# examining features to find important ones that correlate to target var
df.describe()

# encode res -> run correlation
from sklearn.preprocessing import LabelEncoder

le_temp = LabelEncoder()
# converts non numerical--home win, away win, draw into numeric encodings
df['result_encoded'] = le_temp.fit_transform(df['result'])

# quick correlation check
df.corr(numeric_only=True)['result_encoded'].sort_values()

# visualize the distributions
df['HomeGoals'].hist(bins=10)
plt.title('Distribution of Home Goals')
plt.show()