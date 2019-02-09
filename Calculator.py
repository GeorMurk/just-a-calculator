#!/usr/bin/python

#!Basic Calculator

number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
result = number1 + number2 #!The arithmetics can undertake any arithmetic sign (+, -, *, /)

print(result) #!python in this calculation is going to print out as a string

#!To print out in proper calculation

result1 = int(number1) + int(number2)

print(result1) #!Here the result is going to be converted into integers(whole numbers) and any decimal value is going to give an error message

#!To calculate in decimals

result2 = float(number1) + float(number2)

print(result2)

#!Go Ahead and Test
