#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:37:21 2023

@author: tamadaritikashree
"""
# Import the pandas library as pd, used for analysis
import pandas as pd
# Import the matplotlib.pyplot as plt, used for creating plots and charts
import matplotlib.pyplot as plt
# Import the seaborn library for attractive drawing
import seaborn as sns


# Read the CSV file  into a pandas, with the first column used as the index
df = pd.read_csv("International Tourism.csv", index_col=0)


# Define a function called lineplot_travel, used to create line plots 
def linePlot_travel(linePlotData):
    # Create a new figure for line plots
    plt.figure()
    # Set the style of the plot to "Whitegrid"
    sns.set_style("whitegrid")
    
    '''Plot the data for each country using marker("o") for each data point
       df1["Years"] is the x-axis data and 
       df1["Afghanistan","Bangladesh","Bhutan","India", "Maldives", "Nepal",
           Pakistan", "Sri Lanka"] is the y-axis data. 
       Each plot represents a country and a label is assigned to each plot for
       the legend'''
       
    plt.plot(df1["Years"], df1["Afghanistan"], marker="o", label="Afghanistan")
    plt.plot(df1["Years"], df1["Bangladesh"], marker="o", label="Bangladesh")
    plt.plot(df1["Years"], df1["Bhutan"], marker="o", label="Bhutan")
    plt.plot(df1["Years"], df1["India"], marker="o", label="India")
    plt.plot(df1["Years"], df1["Maldives"], marker="o", label="Maldives")
    plt.plot(df1["Years"], df1["Nepal"], marker="o", label="Nepal")
    plt.plot(df1["Years"], df1["Pakistan"], marker="o", label="Pakistan")
    plt.plot(df1["Years"], df1["Sri Lanka"], marker="o", label="Sri Lanka")
    
    
    plt.legend()# Add a legend to the line plot
    plt.title("International Tourism")# Set the title as "International Torism"
    plt.xlabel("Years")# set label for x-axis as "Years"
    plt.ylabel("Expenditure(%)")# set label for y-axis as "Expenditure(%)"
    plt.show()# Show the line Plot
    
    
# Define a function called barPlot_travel, used to create bar plots 
def barPlot_travel(barData):
    # Create a new figure for bar plots of size (16,6)
    plt.figure(figsize=(16, 6))
    
    '''plot a bar chart for the specified dataframe df1 with Years column on 
    x-axis and ["Afghanistan", "Bangladesh", "Bhutan",	"India", "Maldives", 
                "Nepal", "Pakistan", "Sri Lanka"] columns on y-axis'''
                
    df1.plot(x="Years", y=["Afghanistan", "Bangladesh", "Bhutan",	"India", 
                           "Maldives", "Nepal", "Pakistan", "Sri Lanka"],
                 # Specify the type of the plot as bar chart
                 kind="bar", 
                 # Set the title of the plots as "International Tourism"
                 title="International Tourism",
                 # Set label for x-axis as "Years"
                 xlabel="Years", 
                 # Set label for y-axis is "Expenditure(%)"
                 ylabel="Expenditure(%)", 
                 # Show the legend in the bar plot
                 legend=True,
                 # Set the width of the bars to 0.65
                 width=0.65)
    # Show the bar Plot
    plt.show()
                 
             
# Define a function called scatterPlot_travel, used to create scatter plots    
def scatterPlot_travel(scatterData):
    # Create a new figure for scatter plots
    plt.figure()
    
    '''plot a scatter chart for the specified dataframe df1 with Years column 
    on x-axis and ['Afghanistan', 'Bangladesh', 'Bhutan',	'India', 'Maldives',
                   'Nepal', 'Pakistan', 'Sri Lanka'] columns on y-axis'''
                
    plt.scatter(df1["Years"], df1["Afghanistan"], label="Afghanistan")
    plt.scatter(df1["Years"], df1["Bangladesh"], label="Bangladesh")
    plt.scatter(df1["Years"], df1["Bhutan"], label="Bhutan")
    plt.scatter(df1["Years"], df1["India"], label="India")
    plt.scatter(df1["Years"], df1["Maldives"], label="Maldives")
    plt.scatter(df1["Years"], df1["Nepal"], label="Nepal")
    plt.scatter(df1["Years"], df1["Pakistan"], label="Pakistan")
    plt.scatter(df1["Years"], df1["Sri Lanka"], label="Sri Lanka")
    
    plt.legend()# Add a legend to the scatter plot
    plt.title("International Tourism")# Set the title as "International Torism"
    plt.xlabel("Years")# set label for x-axis as "Years"
    plt.ylabel("Expenditure(%)") # set label for y-axis as "Expenditure(%)"
    plt.show()# Show the scatter Plot
    

# Remove the last 5 rows from the Dataframe df to remove null values
df = df.iloc[:-5]
# Drop the specified columns from df1 and assign it to df3
df3 = df.drop(["Country Code", "Series Name", "Series Code"], axis=1)
# Transpose df3 to switch rows and columns and assign it to df_trans
df_trans = df3.transpose()
# Reset the index of df_trans with drop=True and assign it to df2
df2 = df_trans.reset_index(drop=True)
#display first few rows of df2
df2.head()
# Create a pandas series years with specified values and data type
year = pd.Series([2013, 2014, 2015, 2016, 2017,
                 2018, 2019, 2020], dtype=object)
# Add the series year as a new column named "years" to df2
df2["Years"] = year
# Concatenate the last and first part of the dataframe df2 and assign it to df1
df1 = pd.concat([df2.iloc[:, -1:], df2.iloc[:, :-1]], axis=1)


# Function that creates a line plot using the dataframe df1
linePlot_travel(df1)
# Function that creates a bar plot using the dataframe df1
barPlot_travel(df1)
# Function that creates a scatter plot using the dataframe df1
scatterPlot_travel(df1)
