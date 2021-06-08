# List iterations
import time
import pandas
import os
temps = [221, 234, 3400, 230]

new_temps = [temp / 10 for temp in temps]

print(new_temps)

temps = [221, 234, -9999, 230]

# List iterations with if
new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)


def foo(input):
    input = [integer for integer in input if type(integer) == int]
    return input


def foo1(input):
    input = [integer for integer in input
             if integer > 0]
    return input


# List iterations with ifelse
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]


def foo2(input):
    input = [integer if type(integer) == int else 0 for integer in input]
    return input


def foo3(input):
    sum = 0.0
    input = [float(decimal) for decimal in input]
    for x in input:
        sum += 1
    return sum

# Better way for above


def foo4(lst):
    return sum([float(i) for i in lst])


def area(a, b):
    return a * b


def foo5(string1, string2):
    return string1.concatenate(), string2.concatenate()


def mean(*args):
    return args


myfile = open("files/fruits.txt")
content = myfile.read()
myfile.close()

with open("files/fruits.txt") as myfile:
    content = myfile.read()

print(content)

with open("files/vegetables.txt") as myfile:
    content = myfile.read(90)

print(content)


def foo6(character, filepath):
    with open(filepath) as tempfile:
        content = tempfile.read()
        count = content.count(character)
    return count


def appending():
    with open("files/fruits.txt", "a+") as myfile:
        myfile.write("\nOkra")
        myfile.seek(0)
        content = myfile.read()
    print(content)


while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(10)
