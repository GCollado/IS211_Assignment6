"""
1-create two files: conversion.py and tests.py
    -conversions.py holds functions that will do the temperature unit conversions
    -test.py holds all our tests
-----------------------------------------------------
Part1: Create Tests for Celsius Conversion
-----------------------------------------------------
1-convertCelsiusToKelvin() takes a float representing a Celsius measurement, and returns that temperature
 converted to Kelvins
2-convertCelsiusToFahrenheit() takes a float representing a Celsius measurement, and returns the
 temperature converted to Fahrenheit
    -Have it return 0.0
    -Include five test cases for each function
 -----------------------------------------------------
 Part II - Implement the Celsius Conversion Functions
 -----------------------------------------------------
 -Make test your functions and sure they run without errors
 -----------------------------------------------------
 Part III - Repeat
 -----------------------------------------------------
 1. Test again and make sure you have 6 functions
 ------------------------------------------------------
 Par IV - Refactor
 ------------------------------------------------------
 
 """
def convertCelsiusToKelvin(Celsius):
    if type(Celsius) == float:
        return round(Celsius + 273.15, 2)
    else:
        raise NotFloat('The number needs to be a floating point number (ex. 30.0)')
        #print(return round(Celsius + 273.15, 2).())

def convertCelsiusToFahrenheit(Celsius):
    if type(Celsius) == float:
        return round((Celsius*9.0/5.0) + 32,2)
    else:
        raise NotFloat('The number needs to be a floating point number (ex. 273.0)')

class NotFloat(TypeError):
    pass


convertCelsiusToKelvin(300.0)