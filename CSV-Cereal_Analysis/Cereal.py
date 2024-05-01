"""
PROGRAMMER: RYAN PIERCE
DATE:   April 26, 2023
ASSIGNMENT: Homework #9 : Process CSV files for Cereal Analysis 
ALGORITHM: opens csv file and reads out the contents, displaying the lowest fat cereal and highest caloric cereal.
"""
# 1) What is the lowest fat cereal?
# 2) What cereal has the highest calories?

import csv
import os

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Construct the absolute file path to cereal.csv
    csv_file_path = os.path.join(script_dir, 'cereal.csv')
    # Opens the cereal.csv file for reading

    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        # Initialize variables to store the lowest fat and highest calorie cereals
        highest_caloriesBrands = []
        lowest_fatBrands = []
        brand_fat = {}
        brand_calories = {}
        
        # Loops over each row in the csv file
        for row in csv_reader:
            line_count += 1
            # Skips the first two lines which provides variable type information
            if line_count > 2:
                #Creating Dictonaries with Brand names as Keys and Fat/Calories as Values
                brand_fat[str(row[0])] = int(row[5])
                brand_calories[str(row[0])] = int(row[3])
        #Creates List of Fat/Calorie values from Dictionary
        fat_values = brand_fat.values()
        calories_values = brand_calories.values()
        # Variables with Lowest Fat and Highest Calorie Value from lists
        lowest_fat = min(fat_values)
        highest_calories = max(calories_values)

        # Loops Dictionary using List to find brands that equal the lowest fat value and appends them to list
        for brands, fat in brand_fat.items():
            if fat == min(fat_values):
                lowest_fatBrands.append(brands)
        # Loops Dictionary using List to find brands that equal the highest calorie value and appends them to list
        for brands, calories in brand_calories.items():
            if calories == max(calories_values):
                highest_caloriesBrands.append(brands)
    # Joins the contents of the list into a string
    highest_caloriesBrands = " ".join(highest_caloriesBrands)
    lowest_fatBrands = ", ".join(lowest_fatBrands)

    # Prints the answers and additional information
    print(f'Highest Caloric Content is: {highest_calories} Calories')
    print(f'The Highest Caloric Cereal is {highest_caloriesBrands}.')    
    print(f'\nLowest Fat Content is: {lowest_fat} Fat')
    print(f'The Lowest Fat Cereals are {lowest_fatBrands}. ')  

if __name__ == '__main__':
    main()