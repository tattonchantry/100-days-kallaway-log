# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:21:11 2019

@author: Brodie

With this one I am going to attempt to go through the book think python from
here: http://greenteapress.com/thinkpython2/html/index.html
"""

# Chapter 1 - The way of the program exercizes

#%% 1 give invalid syntax with suggestion
print "Hello World"

#%% 2 Gives invalid syntax

print(Hello world")

#%% 3 all work
-2
+2
++2
++++2

#%% 4. In math notation, leading zeros are ok, as in 09. What happens if you
# try this in Python? What about 011?
09  # invalid token
011  #invalid token

#%% 5. What happens if you have two values with no operator between them?

2 5  # invalid syntax

#%% Exercise 1.2. Start the Python interpreter and use it as a calculator.
# 1. How many seconds are there in 42 minutes 42 seconds?

42 * 60 + 42 # 2562

# 2. How many miles are there in 10 kilometers?
# Hint: there are 1.61 kilometers in a mile.

10 / 1.62 # 6.172839...

#%% 3. If you run a 10 kilometer race in 42 minutes 42 seconds
# What is your average pace (time per mile in minutes and seconds)?
# What is your average speed in miles per hour?
import math


def GetVars(km, time):
    t = int(time[:2]) * 60 + int(time[-2:])
    miles = int(km) / 1.62
    minutes = math.floor((t / miles) / 60)  # for one mile
    seconds = round((((t / miles) / 60) % 1) * 60)
    hours = minutes / 60 + seconds / 3600  # for one mile
    print("Hours = {}".format(hours))
    return miles, hours, minutes, seconds


def PrintEm(km, time):
    miles, hours, minutes, seconds = GetVars(km, time)
    mph = 1/hours  # One mile / hours
    print("Average minutes per mile is: {}:{}".format(minutes, seconds))
    print("Average miles per hour is: {}".format(round(mph, 2)))


distance = input("How many kilometers? ")
time = input("What is your time? (mm:ss): ")
PrintEm(distance, time)

#%% 4
