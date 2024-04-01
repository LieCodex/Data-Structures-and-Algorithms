from tabulate import tabulate
import matplotlib.pyplot as plt
from os import path
import time
import numpy as np
import os
import ast
import math


# employees = []
# daily_salary = 0.0
# total = 0.0
# my_data = []
# head = ["name", "position", "address", "company", "period from-to", "hours", "rate", "daily salary"]
# while True:
#     s = Employee(input("Enter Name: "),
#                  input("position: "),
#                  input("address: "),
#                  input("company: "),
#                  input("period from: "),
#                  input("period to: "),
#                  float(input("Hourly rate: ")),
#                  float(input("Hourly duty: ")))
#
#     employees.append(s)
#     tryAgain = input("Do you want to add more employee? Y/N: ").upper()
#     if tryAgain == "N":
#         for employee in employees:
#             my_data.append([employee.name, employee.position, employee.address,employee.company, employee.period_from + "Am - " + employee.period_to + "Pm",employee.hours_duty, employee.hourly_rate, employee.daily_salary() ])
#             total = total + employee.daily_salary()
#         print(tabulate(my_data, headers=head, tablefmt="grid"))
#         print("Total Gross salary: " + str(total))
#         break
#     elif tryAgain == "Y":
#         continue
#     else:
#         print("Invalid Input!!")
#         break
#
# array1 = [100, 2, 3, 4, 50, 6, 7, 9, 10]
# array2 = [23, 25, 32, 44, 56, 66, 97, 79, 101]
#
# for a1 in array1:
#     for a2 in array2:
#         sum = a1 + a2
#         print(f"{a1} + {a2} is: {sum}")
#
# print(array1)
# print()
# for a in array1:
#     print(a)
#
# print()
# print(array1[5])
#
# ans = int(array1[0] + array1[4])
# print(ans)
# duration = []
# start = time.time()
# end = 0
# value = 9
# for i in range(1000):
#     print(i)
#     end = time.time()
#     diff = end - start
#     duration.append(diff)
#
#
# def displayplot():
#     plt.plot(duration)
#     plt.ylabel("Time")
#     plt.xlabel("Data")
#     plt.show()
#
#
# print(duration)
# displayplot()


# numbery = np.random.normal(50,20,1000)
# numberx = np.random.normal(500,20,1000)
#
#
# plt.scatter(numberx, numbery, alpha=0.3, marker="*", s=100)
# plt.show()

valueX = []
numberPick = int(input("LIST OF FUNCTIONS:\n1.) f(x) = x^2 + 7x + 2\n2.) f(x) = 3x + 2\n3.) f(x) = x^2\n4.) f(x) = x^3\n5.) f(x) = x^5\n6.) f(x) = x^3 + 2x^2 + x + 10\n7.) f(x) = x^4 - 3x^3 + 2x^2 - x + 11\n8.) f(x) = sin(x)\n9.) f(x) = cos(x)\n10.) f(x) = x^5 + 4x^4 + x^3 - 2x^2 + 100\n11.) All Functions from 1-10\n\nEnter the number of the function you want to solve: "))
function_expressions = [
    "x^2 + 7x + 2",
    "3x + 2",
    "x^2",
    "x^3",
    "x^5",
    "x^3 + 2x^2 + x + 10",
    "x^4 - 3x^3 + 2x^2 - x + 11",
    "sin(x)",
    "cos(x)",
    "x^5 + 4x^4 + x^3 - 2x^2 + 100"]


with open(".venv/numbers.txt", "r") as file:
    data = file.readlines()
    for line in data:
        valueX.extend([int(x) for x in line.split(',')])


def prob1():
    result = []
    for x in valueX:
        NumHolder = x
        result.append((NumHolder * NumHolder) + (7 * NumHolder) + 2)
    return result
def prob2():#ito yung problem number 2 which is 3x + 2
    result = []#dito mo ilagay yung results
    for x in valueX:#isa isahin mo yung 1-50 which is yung x
        NumHolder = x#number holder will represent 'x'
        result.append((3 * NumHolder) + 2)#nilalagay ko sa result list kung ano man ang result ng code
        #3 *NumberHolder(which represents 'x') + 2, exactly like the problem
    return result#then return the list of results
def prob3():
    result = []
    for x in valueX:
        NumHolder = x
        result.append(NumHolder**2)
    return result
def prob4():
    result = []
    for x in valueX:
        NumHolder = x
        result.append(NumHolder**3)
    return result
def prob5():
    result = []
    for x in valueX:
        NumHolder = x
        result.append(NumHolder**5)
    return result
def prob6():
    result = []
    for x in valueX:
        NumHolder = x
        result.append(NumHolder**3 + (2 * NumHolder**2) + NumHolder + 10)
    return result
def prob7():
    result = []
    for x in valueX:
        NumHolder = x
        result.append(
            NumHolder**4 - (3 * (NumHolder**2 * NumHolder)) + (
                        2 * NumHolder**2) - NumHolder + 11)

    return result
def prob8():
    result = []
    for x in valueX:
        result.append(math.sin(x))

    return result
def prob9():
    result = []
    for x in valueX:
        result.append(math.cos(x))

    return result
def prob10():
    result = []
    for x in valueX:
        NumHolder = x
        result.append(
            (NumHolder**5) + (4 * NumHolder**4) +
            (NumHolder**3) - (2 * NumHolder**2) + 100)

    return result

def createFile(numberEquation):
    if numberEquation == 1:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob1()))
    elif numberEquation == 2:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob2()))
    elif numberEquation == 3:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob3()))
    elif numberEquation == 4:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob4()))
    elif numberEquation == 5:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob5()))
    elif numberEquation == 6:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob6()))
    elif numberEquation == 7:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob7()))
    elif numberEquation == 8:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob8()))
    elif numberEquation == 9:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob9()))
    elif numberEquation == 10:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob10()))
    elif numberEquation == 11:
        with open(".venv/result.txt", "w") as file:
            file.write(str(prob1()))
            file.write("\n")
            file.write(str(prob2()))
            file.write("\n")
            file.write(str(prob3()))
            file.write("\n")
            file.write(str(prob4()))
            file.write("\n")
            file.write(str(prob5()))
            file.write("\n")
            file.write(str(prob6()))
            file.write("\n")
            file.write(str(prob7()))
            file.write("\n")
            file.write(str(prob8()))
            file.write("\n")
            file.write(str(prob9()))
            file.write("\n")
            file.write(str(prob10()))

def readfile():
    results = []
    with open(".venv/result.txt", "r") as file:
        data = file.readlines()
        for line in data:
            results.append(ast.literal_eval(line.strip()))
    return results


def plot_results():
    if numberPick == 11:
        results = readfile()
        for i, result in enumerate(results):
            # Use the function expressions in the labels
            plt.plot(valueX, result, label=f"Problem {i+1}: {function_expressions[i]}")
    elif numberPick < 11:
        results = readfile()
        for i, result in enumerate(results):
            # Use the function expressions in the labels
            plt.plot(valueX, result, label=f"Problem {numberPick}: {function_expressions[numberPick - 1]}")
    plt.xlabel('Number')
    plt.ylabel('Result')
    plt.legend()
    plt.show()

createFile(numberPick)
plot_results()
