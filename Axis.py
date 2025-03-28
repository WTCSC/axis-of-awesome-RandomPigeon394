import pandas as pd
import matplotlib.pyplot as plt

#Data of colors
colors = ['Yellow', 'Orange', 'Green', 'Purple', 'Red']
totals = [624, 566, 612, 591, 573]

df = pd.DataFrame({'Color': colors, 'Count': totals})

average_count = df['Count'].mean()

#Bar graph
plt.figure(figsize=(8, 5))
plt.bar(df['Color'], df['Count'], color=['yellow', 'orange', 'green', 'purple', 'red'])
plt.axhline(average_count, color='black', linestyle='dashed', linewidth=1, label=f'Avg: {average_count:.1f}')
plt.xlabel("Skittle Color")
plt.ylabel("Total Count")
plt.title("Distribution of Skittles Colors")
plt.legend()
plt.show()

#Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(df['Count'], labels=df['Color'], autopct='%1.1f%%', colors=['yellow', 'orange', 'green', 'purple', 'red'])
plt.title("Proportion of Skittles Colors")
plt.show()


most_common = df.loc[df['Count'].idxmax(), 'Color']
least_common = df.loc[df['Count'].idxmin(), 'Color']
print(f"Insight: Yellow Skittles appear to be the most common, while Orange Skittles are the least common.") #Insight
