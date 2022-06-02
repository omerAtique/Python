print("********** Part 1.8.1 **********")

num = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in num:
    print(1/x, ", ")

print("********** Part 1.8.2 **********")

x = 1

while True:
    x = int(input("Enter a positive number: "))

    if x < 0:
        print("Negative numbers not allowed. So try again.")
        continue
    else:
        print(" ")
        while x >= 0:
            
            print(x, "!")
            x-=1
        if(x < 0):
            break

if x == -1:
    print("BLAST OFF!")

print("********** Part 1.8.3 **********")

base = int(input("Enter the base of the number: "))
exp = int(input("Enter the power of the number: "))

sqrtx = 1

for x in range (1, exp+1):
    sqrtx = sqrtx * base

if (exp == 0):
    sqrtx = 1
print("The result is: ", sqrtx)

print("********** Part 1.8.4 **********")

while True:
    number = int(input("Enter a number divisible by 2: "))

    if (number % 2 != 0):
        print("My condolences for your brain. I did not know it was dead.")
        continue
    else:
        print("SHEEEEEEEEESH! about time you passed first grade!")
        break

