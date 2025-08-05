import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data load — use your actual CSV
matches = pd.read_csv('matches.csv')

# 1. Matches per Season
plt.figure(figsize=(10,6))
sns.countplot(data=matches, x='season')
plt.title('Number of Matches Played per Season')
plt.xlabel('Season')
plt.ylabel('Number of Matches')
plt.show()

# 2. Distribution of Match Win Type
def win_type(row):
    if row['win_by_runs'] > 0:
        return 'Runs'
    elif row['win_by_wickets'] > 0:
        return 'Wickets'
    else:
        return 'Other'

matches['win_type'] = matches.apply(win_type, axis=1)
win_counts = matches['win_type'].value_counts()

plt.figure(figsize=(6,6))
win_counts.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Match Results by Win Type')
plt.ylabel('')
plt.show()
