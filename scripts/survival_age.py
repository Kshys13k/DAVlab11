import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("../data/age_plot.csv")
x=df.columns.tolist()
y=(df.iloc[1]/(df.iloc[1]+df.iloc[0])*100).tolist()

# Plotting
plt.figure(figsize=(10,6))
plt.plot(x, y)

# Adding title and labels
plt.title("Survival Rates by Age")
plt.xlabel("Age")
plt.ylabel("Survival Rate [%]")

# Add grid
plt.grid(axis="y", alpha=0.5)

# Display only every other label
plt.xticks(ticks=range(0, len(x), 5), labels=x[::5])

# plt.show()
plt.savefig("../plots/survival_age_plot.png")
