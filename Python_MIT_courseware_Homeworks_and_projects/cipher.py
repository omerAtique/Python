plainText = input("Enter the phrase you want to put the cypher on: ")
cypher = int(input("Enter the key: "))
cypherText = list(plainText)
length = len(plainText)

for x in range(0, length-1):
    cypherText[x] = str(ord(cypherText[x]))
    cypherText[x] = str((int(cypherText[x]) + cypher))
    cypherText[x] = str(chr(int(cypherText[x])))

finalText = ""

for y in cypherText:
    finalText += y

print("The Text when cyphered is: ", finalText)

