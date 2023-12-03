# The goal is to look through the input file and create integer values
# of the first and last integers in each line
# For example, the line: "a1jgbe5" would have an integer value of 15
# Continuing on to the next line, we would find the value
# and add it together to the previous line, keeping a rolling total
# We then return the rolling total

# Solution Below
# --------------------

import os


# Create a list of integers to cross reference as we find them
integerList = ["1","2","3","4","5","6","7","8","9","0"]

rollingTotal = 0

with open("Day1Input.txt", "r") as inputFile:
    for line in inputFile:
        #print(f"Line: {line.strip()}")
        firstInt = ""
        lastInt = ""
        combinedInt = ""
        for char in line:
            if char in integerList:
                firstInt = char
                break
        #print(f"Found the first int: {firstInt}")
        for char2 in line[::-1]:
            if char2 in integerList:
                lastInt = char2
                break
        #print(f"Found the  last int: {lastInt}")

        combinedInt = int(firstInt + lastInt)
        #print(f"Combined int: {combinedInt}")
        
        rollingTotal += combinedInt

print(f"Rolling Total: {rollingTotal}")
