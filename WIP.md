# CQT

## Chapter 0 : 

## Chapter 1 : Unit tests

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

## Ex2 : Leap Year Kata
This short and simple Kata should be performed in pairs using Test Driven Development (TDD).

User Story:

As a user, I want to know if a year is a leap year, So that I can plan for an extra day on February 29th during those years.

Acceptance Criteria:

All years divisible by 400 ARE leap years (so, for example, 2000 was indeed a leap year),
All years divisible by 100 but not by 400 are NOT leap years (so, for example, 1700, 1800, and 1900 were NOT leap years, NOR will 2100 be a leap year),
All years divisible by 4 but not by 100 ARE leap years (e.g., 2008, 2012, 2016),
All years not divisible by 4 are NOT leap years (e.g. 2017, 2018, 2019).

source : https://codingdojo.org/kata/LeapYears/

## Ex3 : Student
Add some unit tests with pytest on student.py class (available in this repository) and then generate a test coverage report using pytest-cov.

## Chapter 2 : Apply Code Quality to a Python Program

## Ex1 : Clean code

Fix 

      def calc(x, y):
        z = x * y
        return z

      def process_data(data):
        total = 0
        for value in data:
            if value > 0:
                total += value
            else:
                total -= value
    
        average = total / len(data)
        return total, average

      def calculate_discount(price):
        if price > 100:
            return price * 0.9
        return price

      def calculate(data):
        result = sum(data) / len(data)
        return result

      def create_order(customer_name, customer_address, product_id, product_quantity, product_price):
        total_price = product_quantity * product_price
        print(f"Order created for {customer_name}, {customer_address}: Product {product_id}, Quantity {product_quantity}, Total {total_price}")


## Ex2 : SOLID principles

 Fix SRP

     class Order:
      def __init__(self, items):
        self.items = items

      def calculate_total(self):
          total = 0
          for item in self.items:
              total += item['price']
          return total

      def print_order(self):
          print("Order details:")
          for item in self.items:
              print(f"{item['name']}: {item['price']}")

  Fix OCP

    class Discount:
      def __init__(self, discount_type):
          self.discount_type = discount_type

      def apply_discount(self, price):
          if self.discount_type == 'percentage':
              return price * 0.9
          elif self.discount_type == 'fixed':
              return price - 10


## Ex3 : Ugly Car

You can find ugly_car.py in this repository.

- Read it
- Run it
- Improve it :)

Tips : Unit tests, PEPs (8 - 20 - 257 - 484 - 526 - 311 - 498...), Formatters, Linters, Code analysis tools


