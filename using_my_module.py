import math
import my_module


# Uppgift 1 (givet)

y = 222
x = 111
x_list = [111, 222, 333, 444]
#print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
#my_module.scope_testing_function(x, x_list)
#print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2 (att skrivas)
my_module.my_function(math.pi)
my_module.my_function(math.pi/2)
# Uppgift 3 (att skrivas)
print(my_module.roll_dice(2))
# Uppgift 4 (att skrivas)
list = [4,1,2,3,3,5,1,1,9,7,8]
print(my_module.my_sort_list(list))
# Uppgift 5 (att skrivas)
print(my_module.bandit_language("jag talar rövarspråket"))
# Uppgift 6 (givet)

animals = {'tiger': ['claws', 'sharp teeth', 'four legs', 'stripes'],
           'elephant': ['trunk', 'four legs', 'big ears', 'gray skin'],
           'human': ['two legs', 'funny looking ears', 'a sense of humor']
           }

# Uppgift 6 (att skrivas)

def make_bandit_dictionary(dict):
    old_keys = []
    new_keys = []
    for key in dict:
        old_keys.append(key)
        new_string = ""
        for letter in key:
            if letter != " ":
                letter += "o" + letter
            
            new_string += letter 
         
        new_keys.append(new_string) 
    for i in range(0,len(new_keys)):
        dict[new_keys[i]] = dict[old_keys[i]]
        del dict[old_keys[i]]
    
make_bandit_dictionary(animals)
print(animals.keys())

