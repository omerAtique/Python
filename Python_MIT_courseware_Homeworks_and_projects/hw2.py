# Name: Muhammad Omer Bin Atique
# Section: -
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######
import math
import random


# **********  Exercise 2.0 ********** 
print("**********  Exercise 2.0 **********")
def f1(x):
    print (x + 1)

def f2(x):
    return (x + 1)

f1(2)
f2(3)
print("**********  Exercise 2.1 **********") 

# Define your function here
##### YOUR CODE HERE #####

def rps(player1):
    if (player1 == player2):
        print("Tie")
    elif(player1 == "rock"):
        if(player2 == "paper"):
            print ("Player 2 wins")
        elif(player2 == "scissors"):
            print ("Player 1 wins")
    elif(player1 == "paper"):
        if(player2 == "rock"):
            print ("Player 1 wins")
        elif(player2 == "scissors"):
            print("Player 2 wins")
    elif(player1 == "scissors"):
        if(player2 == "rock"):
            print("Player 2 wins")
        elif(player2 == "paper"):
            print("Player 1 wins")
# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####
player1 = 'rock'
player2 = 'paper'
rps(player1)

player1 = 'scissors'
player2 = 'paper'
rps(player1)

player1 = 'rock'
player2 = 'rock'
rps(player1)
# ********** Exercise 2.2 ********** 
print("**********  Exercise 2.3 **********")
# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m, n):
    if(m%n == 0):
        return True
    elif(n == 0):
        return False        
    else:
        return False
# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print (is_divisible(10, 5))  # This should return True
print (is_divisible(18, 7))  # This should return False
print (is_divisible(42, 4))  # What should this return?


# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(m, n):
    if(m == n):
        return False
    else:
        return True
# Test cases for not_equal
##### YOUR CODE HERE #####
print(not_equal(3,3))
print(not_equal(4, 5))
print(not_equal(35, 43))
# ********** Exercise 2.3 ********** 
print("**********  Exercise 2.4 **********")
## 1 - multadd function
##### YOUR CODE HERE #####


def multadd(a, b, c):
    return (a*b+c)

print(multadd(2, 4, 5))
print(multadd(6, 1, 2))
print(multadd(7, 4, 7))
## 2 - Equations
##### YOUR CODE HERE #####
angle_test = (math.sin(math.pi/4)) + ((math.cos(math.pi/4))/2)

ceiling_test = math.ceil(276/19) + 2*(math.log(12,7))

# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
print("sin(pi/4) + cos(pi/4)/2 is: ", angle_test)
# print angle_test

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test
print("ceiling(276/19) + 2 log_7(12) is: ", ceiling_test)
## 3 - yikes function
##### YOUR CODE HERE #####
def yikes(x):
    return (x*math.e + (1 - math.e**(-x))**(1/2))

# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)
print(yikes(5))
# ********** Exercise 2.4 **********
print("**********  Exercise 2.4 **********")
## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
    rand_No = random.randint(0, 100)
    print("The generated random no is: ", rand_No)

    if(rand_No % 3 == 0):
        return True
    else:
        return False

# Test Cases
##### YOUR CODE HERE #####

if(rand_divis_3()):
    print("Number is divisible by 3")
else:
    print("Number is not divisible y 3")

if(rand_divis_3()):
    print("Number is divisible by 3")
else:
    print("Number is not divisible y 3")

if(rand_divis_3()):
    print("Number is divisible by 3")
else:
    print("Number is not divisible y 3")


## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####
def roll_dice(no_of_sides, no_of_dice):
    x = 1
    while x <= no_of_dice:
        randRoll = random.randint(1, no_of_sides)
        x+=1
        print(randRoll)
    print("That's all FOLKS!!!")

# Test Cases
##### YOUR CODE HERE #####                            
roll_dice(6, 3)
roll_dice(6, 2)
roll_dice(12, 2)

# ********** Exercise 2.5 **********
print("**********  Exercise 2.5 **********")
# code for roots function
##### YOUR CODE HERE #####   
def roots(a, b, c):
    if(((b**2) - (4*a*c)) < 0):
        print("The roots are complex.")
    else:
        root1 = (-b + (((b**2) - (4*a*c)))**(1/2))/2*a
        root2 = (-b - (((b**2) - (4*a*c)))**(1/2))/2*a
        print("The 2 roots are as follows: ")
        print("root 1: ", root1, "\troot 2: ", root2)
# Test Cases
##### YOUR CODE HERE #####
roots(1, 4, 5)
roots(2, -5, 2)



