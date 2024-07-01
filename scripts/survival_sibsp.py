import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("../data/sibsp_plot.csv")
x=df.columns.tolist()
y=(df.iloc[1]/(df.iloc[1]+df.iloc[0])*100).tolist()

# Set color palette
colors= plt.get_cmap("tab10").colors

# Plotting
plt.figure(figsize=(10,6))
bars = plt.bar(x, y, color=colors[:len(x)], zorder=3)

# Adding title and labels
plt.title("Survival Rates by Sibsp")
plt.xlabel("Sibsp")
plt.ylabel("Survival Rate [%]")


# Adding percentage labels above bars
for bar, percentage in zip(bars, y):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{percentage:.1f}%', ha='center', va='bottom')

# Set y-axis limit
plt.ylim(0, 65)

# Add grid
plt.grid(axis="y", alpha=0.5, zorder=0)

# plt.show()
plt.savefig("../plots/survival_sibsp_plot.png")
