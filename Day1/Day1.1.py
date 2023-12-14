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
        print("--------------------")
        print(f"Line: {line.strip()}")
        firstInt = ""
        lastInt = ""
        firstStringWord = ""
        lastStringWord = ""
        stringIntList = {}
        combinedInt = ""


        numberDict = {
            "one"   : 1,
            "two"   : 2,
            "three" : 3,
            "four"  : 4,
            "five"  : 5,
            "six"   : 6,
            "seven" : 7,
            "eight" : 8,
            "nine"  : 9,
            "zero"  : 0,
        }

        # Find the first integer number
        for index1, int1 in enumerate(line):
            if int1 in integerList:
                firstIntPos = index1
                firstInt = int1
                break

        # Find the last integer number
        for index2, int2 in enumerate(line[::-1]):
            if int2 in integerList:
                lastIntPos = index2
                lastInt = int2
                break

        # Outputs for triage
        print(f"First integer number: {firstInt}")
        print(f"First integer pos: {firstIntPos}")
        print("")
        print(f"Last integer number: {lastInt}")
        print(f"Last integer pos: {lastIntPos}")
        print("")

        # Find the all string numbers and add them to a dictionary
        for word in numberDict.keys():
            if line.find(word) != -1:
                stringIntList[word] = line.find(word)

        # Get the lowest index of the dictionary
        # This would be the lowest value of the key:value pair
        # These return the keys that satisfy the constraints
        if stringIntList:
            firstStringWord = min(stringIntList, key=stringIntList.get)
            firstStringInt = stringIntList[firstStringWord]
        
        # Get the highest index of the dictionary
        if stringIntList:
            lastStringWord = max(stringIntList, key=stringIntList.get)
            lastStringInt = stringIntList[lastStringWord]

        #Outputs for triage
        print(f"First String Word: {firstStringWord}")
        print(f"Last String Word: {lastStringWord}")
        print("")
        print(f"First String Word Pos: {firstStringInt}")
        print(f"Last String Word Pos: {lastStringInt}")
        print("")

        # Check to see what is the earlier number
        if int(firstStringInt) < firstIntPos:
            firstIntPos = int(firstStringInt)

        # Check to see what is the later number
        # Check to see what is the earlier number
        if int(lastStringInt) < lastIntPos:
            lastIntPos = int(lastStringInt)

        # Output for triage
        print(f"Found the first int: {firstIntPos}")
        print(f"Found the  last int: {lastIntPos}")


        combinedInt = int(str(firstIntPos) + str(lastIntPos))
        print(f"Combined int: {combinedInt}")
        
        rollingTotal += combinedInt

print(f"Rolling Total: {rollingTotal}")
