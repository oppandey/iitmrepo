# Importing required libraries
import seaborn as sns
import matplotlib.pyplot as plt
# Loading a sample dataset
#tips = sns.load_dataset("tips")
#print(tips.describe())

# Create a visualization relplot v1
#sns.relplot(
#    data=tips,
#    x="total_bill", y="tip", col="time",
#    hue="smoker", style="smoker", size="size",
#)

# Create a visualization relplot v2
#dots = sns.load_dataset("dots")

#sns.relplot(
#    data=dots, kind="line",
#    x="time", y="firing_rate", col="align",
#    hue="choice", size="coherence", style="choice",
#    facet_kws=dict(sharex=False),
#)

#fmri = sns.load_dataset("fmri")
#sns.relplot(
#    data=fmri, kind="line",
#    x="timepoint", y="signal", col="region",
#    hue="event", style="event",
#)

# Creating a linear regression plot

#tips = sns.load_dataset("tips")
#sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")
#sns.displot(data=tips, x="total_bill", col="time", kde=True)
#sns.displot(data=tips, kind="ecdf", x="total_bill", col="time", hue="smoker", rug=True)
#sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")
#sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)
#sns.catplot(data=tips, kind="bar", x="day", y="total_bill", hue="smoker")

#joint Plot
#penguins = sns.load_dataset("penguins")
#sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")

# Creating a scatter plot
#sns.scatterplot(x='total_bill', y='tip', data=tips)
#sns.barplot(x='day', y='tip', data=tips)

#Selecting only numeric columns
#numeric_tips = tips.select_dtypes(include=['float64', 'int64'])
# Creating a heatmap to visualize correlations
#sns.heatmap(numeric_tips.corr(), annot=True, cmap='coolwarm')

# Pair plot of the tips dataset
#sns.pairplot(tips)
penguins = sns.load_dataset("penguins")
sns.pairplot(data=penguins, hue="species")

# Violin plot to visualize the distribution of tips by day
#sns.violinplot(x='day', y='tip', data=tips)

# Set a different style for the plot
#sns.set_style("whitegrid")
# Creating a scatter plot with colors based on the 'sex' column
#sns.scatterplot(x='total_bill', y='tip', hue='sex', data=tips, palette='coolwarm')

# Display the plot
plt.show()
