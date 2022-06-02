# Name:
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 


from lib2to3.pgen2.token import NAME
import mimetypes


def list_intersection(a, b):
    final_result =[]
    for x in a:
        for y in b:
            if x == y and x not in final_result:
                final_result.append(x)

    print(final_result)

# Define your function here
##### YOUR CODE HERE #####
print("**********  Exercise 3.1 **********")
list_intersection([1,3,5], [5,3,1])
list_intersection([1,3,6,9], [10,14,3,72,9])
list_intersection([2,3], [3,3,3,2,10])
list_intersection([2,4,6], [1,3,5])
# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####

# **********  Exercise 3.2 **********

# Define your function here
def ball_collide(ball1, ball2):
    ##### YOUR CODE HERE #####
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2

    r = r1 + r2

    dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

    if dist <= r:
        return ("The balls do collide.")
    else:
        return ("The balls do not collide.")

# Test Cases for Exercise 3.2
print("**********  Exercise 3.2 **********")
print(ball_collide((0, 0, 1), (3, 3, 1))) # Should be False
print(ball_collide((5, 5, 2), (2, 8, 3))) # Should be True
print(ball_collide((7, 8, 2), (4, 4, 3))) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {'6.321':"Data Structures", '6.221':'Logic Design', '7.322':'Economics'}

def add_class(class_num, desc):
    ##### YOUR CODE HERE #####
    my_classes[class_num] = desc
    

# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')

def print_classes(course):
    ##### YOUR CODE HERE #####
    for x in my_classes.keys():
        if course == x[0]:
            print(x, "-", my_classes[x])

# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####
print("**********  Exercise 3.3 **********")
print_classes('7')
print_classes('6')
# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    ##### YOUR CODE HERE #####
    for x,y in zip(l1,l2):
        comb_dict[y] = x
    return comb_dict

combined_dict = combine_lists(AGES, NAMES) # Finish this line...

def people(age):
    # Use combined_dict within this function...
    req_peps = []
    for x,y in zip(combined_dict.values(), combined_dict.keys()):
        if x == age:
            req_peps.append(y)
    return req_peps
    

# Test Cases for Exercise 3.4 (all should be True)
print("**********  Exercise 3.4 **********")
print(people(18))
print ('Dan' in people(18) and 'Cathy' in people(18))
print ('Ed' in people(19) and 'Helen' in people(19) and 'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19))
print ('Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20))
print (people(21) ==   ['Bob'])
print (people(22) ==   ['Kelly'])
print (people(23) ==   [])

# **********  Exercise 3.5 **********

def zellers(month, day, year):
    ##### YOUR CODE HERE #####
    yearstr = str(year)
    century = int(yearstr[0:2])
    year = int(yearstr[2:4])

    months_dic = {"March":1, "April":2, "May":3, "June":4, "July":5,  "August":6, "September":7, "October":8, "November":9, "December":10, "January":11, "Feburary":12}

    if months_dic[month] == 11 or months_dic[month] == 12:
        year = year - 1

    w = ((13*months_dic[month]) - 1)/5
    x = year/4
    y = century/4
    z = w+x+y+day+year-(2*century)
    r = int(z%7)

    day_dic = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thurday", 5:"Friday", 6:"Saturday"}

    return day_dic[r-1]

# Test Cases for Exercise 3.5
print("**********  Exercise 3.5 **********")
print (zellers("March", 10, 1940) == "Sunday") # This should be True
##### YOUR CODE HERE #####