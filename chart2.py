import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your deliveries.csv data
deliveries = pd.read_csv('deliveries.csv')

# Total runs by batting team
runs_by_team = deliveries.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=runs_by_team.index, y=runs_by_team.values, palette='viridis')
plt.title('Total Runs Scored by Each Batting Team')
plt.xlabel('Batting Team')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Total wides bowled by bowling team
wides_by_team = deliveries.groupby('bowling_team')['wide_runs'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=wides_by_team.index, y=wides_by_team.values, palette='plasma')
plt.title('Total Wides Bowled by Each Bowling Team')
plt.xlabel('Bowling Team')
plt.ylabel('Total Wides')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
