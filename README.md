# CASTILLO_ECE2112_PA_3
## Created by: CASTILLO, Aurabella Macy F.
#### I am a 2nd Year Electronics Engineering Student from the University of Santo Tomas.
#### This is my 3rd Experiment-Programming Assignment for ECE2112 (Advance Programming).
#### The following are the Intended Learning Outcomes for this assignment:
####   1. To identify the codes and functions incorporated in the Pandas library
####   2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library
## **Description**: This Repository contains TWO Python files that mainly revolves around Python Data Analysis
### The following are the things that I have learned in this Programming Assignment:
####   1. You can indicate how many first rows will be indexed by entering the value inside of the "head" Pandas function.
####   2. You can indicate how many last rows will be indexed by entering the value inside of the "tail" Pandas function.
####   3. Differenece of the "loc" and "iloc" Pandas function: "loc" can be used to access data using labels/strings and "iloc" can be used to access data using integers.
####   4. You can index a row with a certain keyword by using "str.contains()" in the "loc" function.
####   5. You can not combine the indexing of more than one rows and then print certain columns that you wanted to see because this will result into a "too much indexers" error for the function once runned. In this case you must locate for the specific rows that you want to obtain first and the you can proceed in locating the specific columns that you want for that value.
## 1st Python File: Castillo_Pandas-P1.py
### **Problem 1**: Using knowledge obtained from the experiment and demonstrations:
#### a. Load the corresponding .csv file into a data frame named cars using pandas
#### b. Display the first five and last five rows of the resulting cars.
#### *Expected Outcomes:*
####   *a. Loaded CSV file converted into a pandas data frame.*
####   *b.1. Indexed Data from the FIRST FIVE rows of the Data Frame*
####   *b.2. Indexed Data from the LAST FIVE rows of the Data Frame*
## 2nd Python File: Castillo_Pandas-P2.py
### **Problem 1**: Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
#### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
#### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
#### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
#### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
#### *Expected Outcomes:*
####   *a. First five rows wih odd-numbered columns.*
####   *b. 'Mazda RX4' Cars.*
####   *c. Numbers of 'cyl' that Camaro Z28 has.*
####   *d. Number of cylinders and the gear types of Mazda RX4 Wag, Ford Pantera L, and Honda Civic*
