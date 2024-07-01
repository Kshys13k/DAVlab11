import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df= pd.read_csv("../data/sibsp_plot.csv")
x_labels=df.columns.tolist()
plot_dict={
    "Died": df.iloc[0].tolist(),
    "Survived": df.iloc[1].tolist()
}

x = np.arange(len(x_labels)) # the label locations
width= 1/3 # width of the bars
multiplier = 0

# Define colors for the bars
colors = {
    "Died": "darkred",
    "Survived": "darkgreen"
}

# Plot
fig, ax = plt.subplots(layout="constrained")

for attribute, measurement in plot_dict.items():
    offset = width * multiplier # calculate offset of placement for each bar
    rects = ax.bar(x+offset, measurement, width, label= attribute, color=colors[attribute]) # create bars for each attribute with proper offset
    ax.bar_label(rects, padding=3) # add labels on top of bars
    multiplier +=1 #change offset for next attribute

# Add title, labels, legend etc
ax.set_title("Number of Survivors and Victims by Sibsp")
ax.set_ylabel("Nuber of people")
ax.set_xticks(x+width/2, x_labels) # add x labels in proper places
ax.legend(loc="upper right", ncols=3)
ax.set_ylim(0,310)

# plt.show()
plt.savefig("../plots/survival_sibsp_plot2.png")