
import copy
import math
import random

# Uppgift 1 (givet)

def scope_testing_function(x, x_list):
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x = 1
    x_list[0] = 1
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x_list = [1, 2, 3, 4]
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    return x

x_list = [11, 22, 33, 44]
x = 11
y = 22
#print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

#scope_testing_function(x, x_list)
#print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2 (att skrivas)
def my_function(x):
    y = 0
    y = (math.sin(x)**2)+(x**2)
    print(y)

# Uppgift 3 (att skrivas)

def roll_dice(n):
    sum  = 0
    for i in range(n):
        d = random.randint(1,6)
        sum += d
    return sum    

     


# Uppgift 4 (att skrivas)
def my_sort_list(list):
    while True:
        switches = 0
        for i in range(0,len(list)-1):
            if list[i] > list[i+1]:
                switches+=1
                oldList = list[i+1]
                list[i+1] = list[i]
                list[i] = oldList
        if switches == 0:
            break
    return list    


# Uppgift 5 (att skrivas)
def bandit_language(string):
    new_string = ""
    for i in string:
        if i  != " ":
            i += "o" + i
            
        new_string += i        
    return new_string



