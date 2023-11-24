# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 13:30:04 2023

@author: deji
"""
import numpy as np
import warnings

warnings.filterwarnings("ignore")


grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
# Use numpy functions to calculate the mean, median, and standard deviation of the grades.
print("Mean of grades: ", np.mean(grades))
print("Median of grades: ", np.median(grades))
print("Standard Deviation of grades: ", np.std(grades))

# Use numpy function to find the maximum and minimum of the grades.
print("Minimum grade: ", np.min(grades))
print("Highest grade: ", np.max(grades))

# Use numpy function to sort the grades in ascending order.
print("Sorting the grades: ", np.sort(grades))

# Use numpy function to find the index of the highest grade in the array.
# -----> Your Solution
print(grades[-3])
# -----> Correction
maximum_grade_index = np.argmax(grades)

# Use numpy function to count the number of students who scored above 90.
# -----> Your Solution
print(grades[grades > 90])
# -----> Correction
count_students_above90 = len(grades[grades > 90])

# Use numpy function to calculate the percentage of students who scored above 90.
print(np.mean(grades > 90)*100)

# Use numpy function to calculate the percentage of students who scored below 75.
print(np.mean(grades < 75)* 100)

# Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
high_performers = grades[grades > 90]
print(high_performers)

# Create a new array called "passing_grades" that contains all the grades above 75.
passing_grades = grades[grades > 75]
print(passing_grades)
