"""
Title: Lab 02 a
Author: Taylor Goodspeed
Date: Aug 24, 2023
"""

# Global Variables
ProfitMargin = 0.23 # this is the anticipated annual profit
ProjectedSales = 0 # starting sales

# Functions
# function to calculate the predicted profit.
def PredictProfit(ProfitMargin, ProjectedSales):
    return ProfitMargin * ProjectedSales


# code body
ProjectedSales = float(input('Enter the projected sales this year:')) # asks user for input to perform the calculation

Result = PredictProfit(ProfitMargin, ProjectedSales)
print(f'the predicted company profit this year is: {Result:,.2f}') #retuns the predidcted profit out to 2 deci.