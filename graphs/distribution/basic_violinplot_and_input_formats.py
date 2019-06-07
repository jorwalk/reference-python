"""
Basic violinplot and input formats
It explains how your input must be formated and which function of seaborn you need to use. Three input formats exist to draw a violinplot:
"""

"""
One numerical variable only
If you have only one numerical variable, you probably better have to make an histogram or a density plot. 
But you can still use the violinplot function to describe the distribution of this variable, as follow:
"""
# library & dataset
import seaborn as sns

df = sns.load_dataset('iris')

# Make boxplot for one group only
sns.violinplot(y=df["sepal_length"])
# sns.plt.show()

"""
One variable and several groups
Usually, violinplots are made on the same situation than boxplots: when you have one numerical variable and several groups. 
It allows to compare values from one group to another. Usually you have 2 columns: one gives the value of the variable, the other the group:
"""
# library & dataset
import seaborn as sns

df = sns.load_dataset('iris')

# plot
sns.violinplot(x=df["species"], y=df["sepal_length"])
# sns.plt.show()


"""
Several variables
Violinplot are also useful to compare several variables.  In the iris dataset, we can compare the first 2 numerical variables:
"""
# library & dataset
import seaborn as sns

df = sns.load_dataset('iris')

# plot
sns.violinplot(data=df.ix[:, 0:2])
# sns.plt.show()
