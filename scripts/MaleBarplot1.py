import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("../data/train.csv")
df1=df[df['Sex']=='male']
df_male=df1[["Sex","Survived"]]
df1=df[df['Sex']=='female']
df_female=df1[["Sex","Survived"]]
x=["Survived","Not survived"]
y=[df_female["Survived"].value_counts().tolist()[1],df_female["Survived"].value_counts().tolist()[0]]

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)



plt.show()