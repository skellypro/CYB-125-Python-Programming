number = 0
numList = []

while not numList:
    number = int(input("Enter a number: "))
    if 0 < number:
        numList.append(number)
else:
    print("List is no longer empty.")
print("Thank you!")