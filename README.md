# CQT

## Chapter 1 : 

## Ex1 : Install prerequisites

     PyCharm
     Python v3.8 +
     virtualenv

Isolated development environment setup :

     python3 -m venv venv
     source venv/bin/activate (Linux)
     venv/Scripts/activate (Windows)

Check :

     python --version

## Chapter 2 : Unit Test and Coverage

## Ex1 : Verlan
Implement a function named "verlan" that takes a string as input and returns a new string
with the following modifications:
- Remove leading and trailing whitespaces.
- Reverse the order of characters in the string.
- Convert all characters to lowercase.

Example:

     input: verlan("  Hello World  ")
     output: "dlrow olleh"

Add units test after implementation.

## Ex2 : Student
Add unit tests on student.py class (available in this repository) and then generate a test coverage report using pytest-cov.

## Chapter 3 : Apply Code Quality to a Python Program

## Ex1 : Ugly Car

You can find ugly_car.py in this repository.

- Read
- Run
- Improve it :)

Tips : Unit tests, PEP, Formatters, Linters, Code analysis tools

## Chapter 4 : Test Driven Development (TDD)

## Ex1 : FizzBuzz Kata
FizzBuzz is a programming challenge. Write a program that prints one line for each number from 1 to 100.\

If the number is a multiple of 3, print "Fizz" instead.\
If the number is a multiple of 5, print "Buzz" instead.\
If the number is a multiple of both 3 and 5, print "FizzBuzz".\
Otherwise, simply print the number itself.

Source:  https://codingdojo.org/kata/FizzBuzz/

## Ex2 : WeatherNow API

Create a simple program that uses an external weather library to fetch and display the current temperature for a given city. (use weather_service.py file in this repository)

Rules:

Temperature feeling:\
Cold: Below 10 degrees Celsius\
Moderate: 10 to 20 degrees Celsius\
Warm: 20 to 30 degrees Celsius\
Hot: Above 30 degrees Celsius

In this world, we consider that only three cities exists : Valenciennes, Paris and Marseille.

Examples :

     Enter the city name: Valenciennes
     Result : { 'town': 'Valenciennes', 'temperature': 5, 'feeling': 'Cold' }

     Enter the city name: Marseille
     Result : { 'town': 'Marseille', 'temperature': 25, 'feeling': 'Warm' }

Errors management:

Implement error handling to manage unknown city.

Example :

     Enter the city name: Tokyo
     Result : city not found

Implement error handling to manage exceptions that may occur during the temperature retrieval process.

Example :

     Enter the city name: Valenciennes
     Result : temporary error
     
