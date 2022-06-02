def is_palindrome(pali):
    is_pali = False
    for x in range(0, len(pali)):
        if pali[x] == pali[-x-1]:
            is_pali = True
        else:
            is_pali = False
            break
    
    return is_pali

print(is_palindrome("is si"))

print(is_palindrome("able was i ere i saw elba"))

print(is_palindrome("yummuy"))

print(is_palindrome("a"))

print(is_palindrome("anna"))