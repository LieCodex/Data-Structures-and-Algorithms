# ignore this file, it has no relevance what so ever
# class Employee:
#     name = ''
#     address = 'S'
#     company = ''
#     period_from = ''
#     period_to = ''
#     position = ''
#     hourly_rate = 0.0
#     hours_duty = 0.0
#
#     def __init__(self, name, position, address, company, period_from, period_to, hourly_rate, hours_duty):
#         self.name = name
#         self.position = position
#         self.address = address
#         self.company = company
#         self.period_to = period_to
#         self.period_from = period_from
#         self.hours_duty = hours_duty
#         self.hourly_rate = hourly_rate
#
#     def daily_salary(self):
#         return self.hours_duty * self.hourly_rate
import matplotlib.pyplot as plt
import math
import ast

valueX = []
choose_number = int(input("LIST OF FUNCTIONS:\n1.) f(x) = x^2 + 7x + 2\n2.) f(x) = 3x + 2\n3.) f(x) = x^2\n4.) f(x) = x^3\n5.) f(x) = x^5\n6.) f(x) = x^3 + 2x^2 + x + 10\n7.) f(x) = x^4 - 3x^3 + 2x^2 - x + 11\n8.) f(x) = sin(x)\n9.) f(x) = cos(x)\n10.) f(x) = x^5 + 4x^4 + x^3 - 2x^2 + 100\n11.) All Functions from 1-10\n\nEnter the number of the function you want to solve: "))

with open('.venv/numbers.txt', 'r') as file:
    data = file.readlines()
    for d in data:
        valueX.extend([int(value) for value in d.split(',')])

def eq1():
    result = []
    for x in valueX:
        value = x
        result.append((value * value) + (7 * value) + 2)
    return result

def eq2():
    result = []
    for x in valueX:
        value = x
        result.append((3 * value) + 2)
    return result

def eq3():
    result = []
    for x in valueX:
        value = x
        result.append((value * value))
    return result

def eq4():
    result = []
    for x in valueX:
        value = x
        result.append((value * value * value))
    return result

def eq5():
    result = []
    for x in valueX:
        value = x
        result.append((value * value * value * value * value))
    return result

def eq6():
    result = []
    for x in valueX:
        value = x
        result.append((value * value * value) + (2 * value * value) + value + 10)
    return result

def eq7():
    result = []
    for x in valueX:
        value = x
        result.append((value * value * value * value) - (3 * value * value * value) + (2 * value * value) - value + 11)
    return result

def eq8():
    result = []
    for x in valueX:
        value = x
        result.append(math.sin(math.radians(value)))
    return result

def eq9():
    result = []
    for x in valueX:
        value = x
        result.append(math.cos(math.radians(value)))
    return result

def eq10():
    result = []
    for x in valueX:
        value = x
        result.append((value * value * value * value * value) + (4 * value * value * value * value) + (value * value * value) - (2 * value * value) + 100)
    return result

def createFile(equation_number):
    with open(".venv/function_result.txt", "w") as file:
        if equation_number == 1:
            file.write("f(x) = x^2 + 7x + 2:\n")
            file.write(str(eq1()))
        elif equation_number == 2:
            file.write("f(x) = 3x + 2:\n")
            file.write(str(eq2()))
        elif equation_number == 3:
            file.write("f(x) = x^2:\n")
            file.write(str(eq3()))
        elif equation_number == 4:
            file.write("f(x) = x^3:\n")
            file.write(str(eq4()))
        elif equation_number == 5:
            file.write("f(x) = x^5:\n")
            file.write(str(eq5()))
        elif equation_number == 6:
            file.write("f(x) = x^3 + 2x^2 + x + 10:\n")
            file.write(str(eq6()))
        elif equation_number == 7:
            file.write("f(x) = x^4 - 3x^3 + 2x^2 - x + 11:\n")
            file.write(str(eq7()))
        elif equation_number == 8:
            file.write("f(x) = sin(x):\n")
            file.write(str(eq8()))
        elif equation_number == 9:
            file.write("f(x) = cos(x):\n")
            file.write(str(eq9()))
        elif equation_number == 10:
            file.write("f(x) = x^5 + 4x^4 + x^3 - 2x^2 + 100:\n")
            file.write(str(eq10()))
        elif equation_number == 11:
            file.write("f(x) = x^2 + 7x + 2:\n")
            file.write(str(eq1()))
            file.write("\n\n")
            file.write("f(x) = 3x + 2:\n")
            file.write(str(eq2()))
            file.write("\n\n")
            file.write("f(x) = x^2:\n")
            file.write(str(eq3()))
            file.write("\n\n")
            file.write("f(x) = x^3:\n")
            file.write(str(eq4()))
            file.write("\n\n")
            file.write("f(x) = x^5:\n")
            file.write(str(eq5()))
            file.write("\n\n")
            file.write("f(x) = x^3 + 2x^2 + x + 10:\n")
            file.write(str(eq6()))
            file.write("\n\n")
            file.write("f(x) = x^4 - 3x^3 + 2x^2 - x + 11:\n")
            file.write(str(eq7()))
            file.write("\n\n")
            file.write("f(x) = sin(x):\n")
            file.write(str(eq8()))
            file.write("\n\n")
            file.write("f(x) = cos(x):\n")
            file.write(str(eq9()))
            file.write("\n\n")
            file.write("f(x) = x^5 + 4x^4 + x^3 - 2x^2 + 100:\n")
            file.write(str(eq10()))

def results_plot():
    with open(".venv/function_result.txt", "r") as file:
        data = file.readlines()

    if choose_number == 11:
        results_1_10 = [ast.literal_eval(line.split(":")[1].strip()) for line in data[:10] if ":" in line]
        result_11 = ast.literal_eval(data[10].split(":")[1].strip()) if ":" in data[10] else None

        # Plot equations 1-10
        for i, line in enumerate(data[:10], start=1):
            if ":" in line:
                result = ast.literal_eval(line.split(":")[1].strip())
                function_expression = line.split(":")[0].strip()[len("f(x) = "):]
                plt.plot(valueX, result, label=f"Function {i}: {function_expression}")

        # Plot equation 11
        if result_11 is not None:
            plt.plot(valueX, result_11, label="All Functions from 1-10", linestyle='--')

    else:
        line = data[0]
        if ":" in line:
            result = ast.literal_eval(line.split(":")[1].strip())
            function_expression = line.split(":")[0].strip()[len("f(x) = "):]
            plt.plot(valueX, result, label=f"Function Result: {function_expression}")

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(loc='best')
    plt.show()

createFile(choose_number)
results_plot()
