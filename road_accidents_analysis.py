# -*- coding: utf-8 -*-
"""Road Accident Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tgoTl0iIz3ebCgz-bqh4IqTJ6Pcpo-iZ
"""

#Loading the dataset
df= pd.read_csv("dft-road-casualty-statistics-casualty-provisional-mid-year-unvalidated-2022 (1).csv")
#Display the first few rows of the Dataframe
df.head()

#linear algebra
import numpy as np
#data processing
import pandas as pd
#For visualization
import matplotlib.pyplot as plt
import seaborn as sns

#Shape of the dataset
df.shape

#Checking datatypes of the columns
df.dtypes

#Checking for missing values
df.isnull().sum()

#Descriptive statistics of the numeric columns
df.describe().transpose()

#Count of unique values for each column
df.nunique()

df.value_counts("casualty_severity")

#Plotting the distribution of accident severities
plt.figure(figsize= (8,6))
sns.countplot(x='casualty_severity', data= df)
plt.title('Distribution of Accident severities')
plt.xlabel('Casualty Severity')
plt.ylabel('count')
plt.show()

"""According to above graph high casualty severity(fatal) accidents are too high as compare to low casualty severity accidents."""

#Plotting the relationship between casualty severity and age band
plt.figure(figsize=(10,8))
sns.boxplot(x= 'casualty_severity',y= 'age_of_casualty',data =df)
plt.title('Casualty severity by age of casualty')
plt.xlabel('Casualty Severity')
plt.ylabel('Age of Casualty')
plt.show()

"""From the above graph, the age band of 20-45(youngsters) are the victim of high casualty severity accidents."""

#Plotting the relationship between casualty severity and gender
plt.figure(figsize= (8,6))
sns.countplot(x= 'casualty_severity',hue= 'sex_of_casualty',data= df)
plt.title('Casualty severity by Gender')
plt.xlabel('Casualty Severity')
plt.ylabel('Count')
plt.legend(title= 'Sex of Casualty',labels=['Unknown','Male','Female'])
plt.show()

"""From the above graph, the males are facing more number of accidents and their casualty severity is also high."""

#Plotting the relationship between casualty severity and casualty class
plt.figure(figsize=(8,6))
sns.countplot(x= 'casualty_severity',hue= 'casualty_class',data= df)
plt.title('Casualty Severity by Casualty Class')
plt.xlabel('Casualty Severity')
plt.ylabel('Count')
plt.legend(title= 'Casualty Class',labels= ['Driver','Passenger','Pedestrian'])
plt.show()

"""From the above graph, drivers are the victim of more casualty severity accidents than passenger and pedestrian."""

#Count the no of records with negative ages
negative_age_count= df[df['age_of_casualty']<0].shape[0]
negative_age_count

#Count of no of records with undefined gender values
undefined_gender_count= df[(df['sex_of_casualty']==-1)|(df['sex_of_casualty']==9)].shape[0]
undefined_gender_count

#Exclude records with negative ages or undefined gender values
df_clean= df[(df['age_of_casualty']>=0)& ((df['sex_of_casualty']==1)|(df['sex_of_casualty']==2))]
df_clean

# Plotting the distribution of accidents by gender
plt.figure(figsize=(8, 6))
sns.countplot(x='sex_of_casualty', data=df_clean)
plt.title('Distribution of Accidents by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks([0, 1], ['Male', 'Female'])
plt.show()

"""From the above graph,males are facing more number of accidents than females."""

df.value_counts('pedestrian_road_maintenance_worker')

#Plotting the distribution of Age_of_Casualty values
plt.figure(figsize=(10,8))
sns.histplot(df_clean['age_of_casualty'],bins= 20,kde= True)
plt.title('Distribution of Age of Casualty')
plt.xlabel('Age of Casualty')
plt.ylabel('Count')
plt.show()

"""From the above graph, youngsters of age 18-35 are facing more number of accidents than other age groups."""

# Select numeric columns
numeric_columns = df.select_dtypes(include=[np.number])

# Calculate the correlation matrix for numeric variables
corr_matrix = numeric_columns.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('Correlation Matrix of Numeric Variables')
plt.show()

"""The above graph shows correlations between factors."""