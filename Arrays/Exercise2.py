#Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

maxNumber = int(input("Enter a number: "))


oddList = []

for i in range(1, maxNumber):
    if i % 2 != 0:
        oddList.append(i)
    i += 1


print(oddList)