import pandas as pd
import matplotlib.pyplot as plt

# load the SuperStore dataset
SuperStore_df = pd.read_csv("SuperStore.csv")

# define a function for univariate analysis
def univariate_analysis(data, column):

    # plot a histogram of the data
    plt.hist(data[column], bins=10)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {column}")
    plt.show()

    # plot a boxplot of the data
    plt.boxplot(data[column])
    plt.xlabel(column)
    plt.ylabel("Value")
    plt.title(f"Boxplot of {column}")
    plt.show()

    # print summary statistics of the data
    print(f"Summary statistics of {column}:")
    print(data[column].describe())

# perform univariate analysis on all specified columns
columns = ["Row ID","Postal Code","Sales"]
for col in columns:
    univariate_analysis(SuperStore_df, col)