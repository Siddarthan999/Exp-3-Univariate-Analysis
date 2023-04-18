# Exp-3-Univariate-Analysis

# AIM

To read the given data and perform Univariate Analysis.

# Explanation

Univariate analysis explores each variable in a data set, separately. It looks at the range of values, as well as the central tendency of the values. It describes the pattern of response to the variable. It describes each variable on its own.
# ALGORITHM

# STEP 1

Read the given Data

# STEP 2

Get the information about the data

# STEP 3

Handle missing values

# STEP 4

Perform basic descriptive statistics

# STEP 5

Visualize the data

# CODE FOR “diabetes.csv”

import pandas as pd

import matplotlib.pyplot as plt

#load the diabetes dataset

diabetes_df = pd.read_csv("diabetes.csv")

#define a function for univariate analysis

def univariate_analysis(data, column):

    #plot a histogram of the data
    
    plt.hist(data[column], bins=10)
    
    plt.xlabel(column)
    
    plt.ylabel("Frequency")
    
    plt.title(f"Histogram of {column}")
    
    plt.show()

    #plot a boxplot of the data
    
    plt.boxplot(data[column])
    
    plt.xlabel(column)
    
    plt.ylabel("Value")
    
    plt.title(f"Boxplot of {column}")
    
    plt.show()

    #print summary statistics of the data
    
    print(f"Summary statistics of {column}:")
    
    print(data[column].describe())

#perform univariate analysis on all specified columns

columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]

for col in columns:

    univariate_analysis(diabetes_df, col)
    
# OUTPUT
![image](https://user-images.githubusercontent.com/91734840/230855369-b966017d-4782-47a9-b46b-278fa1537442.png)
![image](https://user-images.githubusercontent.com/91734840/230855499-6716b7c7-5b7d-4d19-8f5c-2d5df37dea60.png)
![image](https://user-images.githubusercontent.com/91734840/230855537-a2d976cc-1fc1-4d2f-8bc6-42cc0301bc92.png)
![image](https://user-images.githubusercontent.com/91734840/230855581-f14f3eb5-dab8-4266-b709-3e2a33963940.png)
![image](https://user-images.githubusercontent.com/91734840/230855602-b186aaba-1696-4583-9222-1b64cdff86b7.png)
![image](https://user-images.githubusercontent.com/91734840/230855621-c8282318-ad17-40a2-97db-cfef00752f39.png)
![image](https://user-images.githubusercontent.com/91734840/230855639-3da5ca9f-67fb-454b-a89c-4756ed809c7a.png)
![image](https://user-images.githubusercontent.com/91734840/230855651-f2cddc54-a16a-49a7-8573-3fe4151523c2.png)
![image](https://user-images.githubusercontent.com/91734840/230855672-f6d7ac55-1927-4f5d-940a-a954a1fc2239.png)
![image](https://user-images.githubusercontent.com/91734840/230855694-07bdd877-c6fc-4a55-b67c-db2b1e625e66.png)
![image](https://user-images.githubusercontent.com/91734840/230855709-238b0c7a-a28e-41d8-9738-ba2de1d60bbe.png)
![image](https://user-images.githubusercontent.com/91734840/230867638-5279abfd-e462-4258-ab42-7a0fc387a23b.png)
![image](https://user-images.githubusercontent.com/91734840/230867668-9637e5c8-f6e0-4561-9060-9a9bee2dc01e.png)


 # CODE FOR "SuperStore.csv"

import pandas as pd

import matplotlib.pyplot as plt

#load the SuperStore dataset

SuperStore_df = pd.read_csv("SuperStore.csv")

#define a function for univariate analysis

def univariate_analysis(data, column):
    #plot a histogram of the data
    
    plt.hist(data[column], bins=10)
    
    plt.xlabel(column)
    
    plt.ylabel("Frequency")
    
    plt.title(f"Histogram of {column}")
    
    plt.show()

    #plot a boxplot of the data
    
    plt.boxplot(data[column])
    
    plt.xlabel(column)
    
    plt.ylabel("Value")
    
    plt.title(f"Boxplot of {column}")
    
    plt.show()

    #print summary statistics of the data
    
    print(f"Summary statistics of {column}:")
    
    print(data[column].describe())

#perform univariate analysis on all specified columns

columns = ["Row ID","Postal Code","Sales"]

for col in columns:

    univariate_analysis(SuperStore_df, col)

# OUTPUT
![image](https://user-images.githubusercontent.com/91734840/230867940-19505813-3296-46cb-bbe3-de0a95fc1081.png)
![image](https://user-images.githubusercontent.com/91734840/230868039-b357408c-f527-48d9-8614-6db1a378ae7c.png)
![image](https://user-images.githubusercontent.com/91734840/230868052-de876301-85c9-4d4e-9ce9-10b4a90fd9cf.png)
![image](https://user-images.githubusercontent.com/91734840/230868069-e056178a-989e-488b-95a5-94626c952204.png)
![image](https://user-images.githubusercontent.com/91734840/230868085-0dba285c-752b-46ae-96bd-510a7516d0a5.png)
![image](https://user-images.githubusercontent.com/91734840/230868108-50a54754-2d8b-44cc-92fc-02edf28a2f5b.png)
![image](https://user-images.githubusercontent.com/91734840/230868127-b4f95ed3-8a23-438d-8c0e-aa1f88d49258.png)

# RESULT

Thus,to read the given data and perform Outlier Detection and Removal has been performed successfully.

