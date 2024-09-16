{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3d8d01ee-722e-40ee-9062-e468def09c42",
   "metadata": {},
   "source": [
    "### Programming Assignment 2 - Python Data Analysis (PANDAS)\n",
    "#### By: CASTILLO, Aurabella Macy F.\n",
    "#### Section: 2ECE-C"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1c0d68d6-19e7-40b6-98e9-2a40884b242b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Access the Pandas Library\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f507f9a1-757b-4525-9270-eaa1691a1730",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Access the required csv file for this Programming Assignment\n",
    "cars=pd.read_csv('cars.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf13a73b-a541-42f4-99f1-5eb5df38f890",
   "metadata": {},
   "source": [
    "#### *Problem 2*: Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.\n",
    "#### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.\n",
    "#### *Expected Output: First five rows wih odd-numbered columns*.."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c44750f5-bd56-41f9-ad71-70c234060049",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.875</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>21.4</td>\n",
       "      <td>6</td>\n",
       "      <td>258.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.08</td>\n",
       "      <td>3.215</td>\n",
       "      <td>19.44</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Valiant</td>\n",
       "      <td>18.1</td>\n",
       "      <td>6</td>\n",
       "      <td>225.0</td>\n",
       "      <td>105</td>\n",
       "      <td>2.76</td>\n",
       "      <td>3.460</td>\n",
       "      <td>20.22</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Merc 240D</td>\n",
       "      <td>24.4</td>\n",
       "      <td>4</td>\n",
       "      <td>146.7</td>\n",
       "      <td>62</td>\n",
       "      <td>3.69</td>\n",
       "      <td>3.190</td>\n",
       "      <td>20.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Merc 280</td>\n",
       "      <td>19.2</td>\n",
       "      <td>6</td>\n",
       "      <td>167.6</td>\n",
       "      <td>123</td>\n",
       "      <td>3.92</td>\n",
       "      <td>3.440</td>\n",
       "      <td>18.30</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
       "1   Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
       "3  Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
       "5         Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0     3   \n",
       "7       Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0     4   \n",
       "9        Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0     4   \n",
       "\n",
       "   carb  \n",
       "1     4  \n",
       "3     1  \n",
       "5     1  \n",
       "7     2  \n",
       "9     4  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Function for locating all odd-numbered rows\n",
    "odd_rows=cars.iloc[1::2] #This will start with index 1 and obtain the odd rows by skipping every other row\n",
    "\n",
    "#Pandas function to index the first five rows\n",
    "odd_rows.head(5)\n",
    "#Note: You can change how many first rows will be indexed by specifying it inside the parentheses"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c75755ce-8144-47cf-886d-dcfee7548ed8",
   "metadata": {},
   "source": [
    "#### *Problem 2*: Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.\n",
    "#### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.\n",
    "#### *Expected Output: 'Mazda RX4' Cars*."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a33cda4c-ae33-47a8-b1db-8b0e8603c0eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
      "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4\n"
     ]
    }
   ],
   "source": [
    "#Pandas function to locate the rows where 'Model' is 'Mazda RX4'\n",
    "mazda_rx4_cars=cars.loc[cars['Model']=='Mazda RX4']\n",
    "#If you want to include any row containing \"Mazda RX4\" then you can put \".str.contains('Paris')\" right after the \"['Model']\"\n",
    "\n",
    "#Print the rows\n",
    "print(mazda_rx4_cars)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3a0b137b-a0f9-4609-8a23-5042f478b6e0",
   "metadata": {},
   "source": [
    "#### *Problem 2*: Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.\n",
    "#### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?\n",
    "#### *Expected Output: Numbers of 'cyl' that Camaro Z28 has.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8660a49e-8ce7-4df8-b9d3-a666cdb2e7d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    cyl\n",
      "23    8\n"
     ]
    }
   ],
   "source": [
    "#Pandas function to know how many 'cyl' does the 'Camaro Z28' have\n",
    "cyl_of_CamaroZ28=cars.loc[(cars['Model']=='Camaro Z28'), ['cyl']] #This filters the column of the cylinder specific to the Model indicated\n",
    "\n",
    "#Print how many 'cyl' does the 'Camaro Z28' have\n",
    "print(cyl_of_CamaroZ28)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20cec781-8758-47e2-ac4b-f27cedd95750",
   "metadata": {},
   "source": [
    "#### *Problem 2*: Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.\n",
    "#### d.Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.\n",
    "#### *Expected Output: Number of cylinders and the gear types of Mazda RX4 Wag, Ford Pantera L, and Honda Civic*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "078a9525-29f1-4af4-9371-dd9407bb9b74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             Model  cyl  gear\n",
      "1    Mazda RX4 Wag    6     4\n",
      "18     Honda Civic    4     4\n",
      "28  Ford Pantera L    8     5\n"
     ]
    }
   ],
   "source": [
    "#Pandas function to locate Mazda RX4 Wag, Ford Pantera L, and Honda Civic\n",
    "needed_cars=cars.loc[(cars['Model']=='Mazda RX4 Wag')|(cars['Model']=='Ford Pantera L')|(cars['Model']=='Honda Civic')]\n",
    "#You can not combine the needed columns for specific indices because there will be too much levels of indexing in the code\n",
    "\n",
    "#Pandas fucntion to locate the 'cyl' and 'gear' for the needed cars\n",
    "cyl_and_gear=needed_cars[['Model','cyl','gear']]\n",
    "\n",
    "#Print the 'cyl' and 'gear' of Mazda RX4 Wag, Ford Pantera L, and Honda Civic\n",
    "print(cyl_and_gear)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
