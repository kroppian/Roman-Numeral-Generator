#!/usr/bin/python
import sys

# todo: iiiv should not equal 2. 

numeralValues = {"I": 1, "V": 5, "X": 10,"L":50,"C":100,"D": 500,"M":1000}

if len(sys.argv) != 2:

    print("Please enter a numeral!")
    exit(1)

def digitizeLatin(numeralIn):

    numeralIn = numeralIn.upper()
    
    currentHighestVal=0    

    # Find the first position of the largest character
    for currentNumIndex in range(0,len(numeralIn)):

        currentNum = numeralIn[currentNumIndex]

        currentNumeralVal = numeralValues[currentNum]

        if currentNumeralVal > currentHighestVal:

            currentHighestVal = currentNumeralVal

            currentHighestIndex = currentNumIndex

    # How many characters to the right are the same as the largest? 
    highestVal = currentHighestVal
    highestNumeral = numeralIn[currentHighestIndex]
    highestIndex = currentHighestIndex 

    currentNumIndex = currentHighestIndex 

    magnitudeOfHighestNumeral = 0 

    while currentNumIndex < len(numeralIn) and numeralIn[currentNumIndex] == highestNumeral:

        magnitudeOfHighestNumeral += 1

        currentNumIndex += 1

    if magnitudeOfHighestNumeral > 3:

        print("Invalid numeral. Too many " + highestNumeral + " characters!")

        exit(1)

    # print (str(currentHighestVal) +  " at " + str(currentHighestIndex) + " for length " + str(magnitudeOfHighestNumeral))

    # to the running total, add the lagest position multiple the number of occurences there are of it 
    runningTot = highestVal * magnitudeOfHighestNumeral

    # subtract the numerals to the left

    leftNumerals = numeralIn[:highestIndex]

    if len(leftNumerals) != 0: 

        runningTot = runningTot - digitizeLatin(leftNumerals)

    # add the numerals to the right
    rightNumerals= numeralIn[highestIndex + magnitudeOfHighestNumeral  :]

    if len(rightNumerals) != 0:

        runningTot = runningTot + digitizeLatin(rightNumerals)

    return runningTot

input = sys.argv[1] 

print (digitizeLatin(input))



