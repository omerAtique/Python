# Name:
# Section:
# strings_and_lists.py

from tokenize import Double


print("**********  Exercise 2.7 **********")

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print ("sum_all of [4, 3, 6] is:", sum_all([4, 3, 6]))
print ("sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4]))


def cumulative_sum(number_list):
    # number_list is a list of numbers
    ##### YOUR CODE HERE #####
        for num in number_list:
            ind = number_list.index(num)
            if(ind == 0):
                continue
            num += number_list[ind-1]
            number_list[ind] = num
        return number_list


# Test Cases
##### YOUR CODE HERE #####

print("Cumulative sum of [4,3,6]: ", cumulative_sum([4, 3, 6]))

print ("**********  Exercise 2.8 **********")

def report_card():
    noOfClasses = int(input("How many classes did you take? "))
    i = 1
    classList = []
    gradeList = []
    while i <=noOfClasses:
        className = input("What is the name of this classs? ")
        grade = float(input("What was your grade in this class? "))
        classList.append(className)
        gradeList.append(grade)
        i+=1

    print("REPORT CARD: ")
    
    for (cl, gl) in zip(classList, gradeList):
        print(cl," - ", gl)

    sum = 0
    for gl in gradeList:
        sum+=gl

    print("OVER ALL GRADE: ", sum/noOfClasses)    
    ##### YOUR CODE HERE #####
# report_card()

# Test Cases
## In comments, show the output of one run of your function.

print ("**********  Exercise 2.9 **********")

# Write any helper functions you need here.
##### YOUR CODE HERE #####
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def pig_latin(word):
    # word is a string to convert to pig-latin
    wordList = list(word)
    isVowel = False
    for n in vowels:
        if n == wordList[0]:
            isVowel = True
            break

    if isVowel == True:
        temp = wordList[0]
        wordList.remove(wordList[0])
        wordList.append(temp)
        wordList.append("ay")
        

    else:
        wordList.append("hay")
        
    print(''.join(wordList))
# Test Cases
##### YOUR CODE HERE #####
pig_latin("Omer")
pig_latin("Sheeeesh")
pig_latin("A.Hitler is pog")

print ("**********  Exercise 2.10 **********")
# Test Cases
##### YOUR CODE HERE #####
newlist = [x**3 for x in range(0, 10)]
print(newlist)

coinFlips = [x + y for x in ["H", "T"] for y in ["H", "T"]]
print(coinFlips)

def vowelsL(word):
    word = list(word)
    vowelsList = [x for x in vowels for y in word if x == y]
    print(vowelsList)

vowelsL("Omer")
vowelsL("AMARICA IS SHIT")

listC = [x*y for x in [10,20,30] for y in [1,2,3]]
print(listC)
# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 