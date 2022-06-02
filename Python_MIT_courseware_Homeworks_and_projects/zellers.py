while True:
    month = int(input("Enter month as a number (1 - 12): "))

    if month < 1 or month > 12:
        print ("INVALID INPUT PLZ TRY AGAIN!")
        continue
    else:
        break

while True:
    day = int(input("Enter day as a number (1-31): "))

    if day < 1 or day > 31:
        print("INVALID INPUT PLZ TRY AGAIN!")
        continue
    else:
        break

year = input("Enter year as a number: ")



century = int(year[0:2])
year = int(year[2:4])



months_dic = {1:"March", 2:"April", 3:"May", 4:"June", 5:"July", 6: "August", 7:"September", 8:"October", 9:"November", 10:"December", 11:"January", 12:"Feburary"}

if month == 11 or month == 12:
    year = year - 1

w = ((13*month) - 1)/5
x = year/4
y = century/4
z = w+x+y+day+year-(2*century)
r = int(z%7)

day_dic = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thurday", 5:"Friday", 6:"Saturday"}

print("The day of birth is: ", day_dic[r-1])