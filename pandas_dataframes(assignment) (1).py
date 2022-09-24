# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:21:15 2020

@author: john.hanks
"""

# Good pandas tutorial here:
# https://data-flair.training/blogs/pandas-tutorial/
# Use this reference to guide you through the assignment

import pandas as pd

# you will need to change the path for your computer
data = pd.read_csv("")

# Print the column names?


# print the data types for each column


# Print the size of the data set, the # of rows and columns


# use the head method and print the first 8 rows of the data set


# With dataframes columns are variables and rows are observations.  Print the first 5 observations for 
# the ' Acc X' column.  In pandas this is a called a series with the "index". Note in the print out there is no
# column heading, so it's not a dataframe. 

# To make a new dataframe that includs the column names (which could be used as variables) use double brackets
# an example, newDataFrame = data[[' Acc X]]

# Make a new data frame called accData for the columns labeled " Acc X", " Acc Y, " Acc Z"

# print the head of the new data frame accData

# print out consecutive rows 2 to 5 of the dataframe accData


# Slice the data using ".loc"
# make a list of two or more rows that are not consecutive and then pass the list into the accData dataframe to return a sliced data frame


# using iloc print a sub-section of data for rows 1 to 5 just the Acc X and Acc Y columns


# What to remember:
# .loc is for selecting consecutive rows
# .iloc is for slicing consecitive rows and consecutive columns (a subsection of the dataframe)

# You can operate on colums using various funtions and math operations 
# Sort the dataframe by the Acc X column and call the new dataframe using one line of code


# rename " Acc X" column so it doesn't have any spaces in the name


# Use the drop method to drop the 'Index' column from the data dataframe


# change the datatype of "AccX" column in the data dataframe to floating point


# for the data dataframe add a new column called "Xthresold" which is 10% of the AccX column variable


# Use the describe method on the data dataframe to review the statistics

