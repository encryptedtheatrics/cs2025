# Q1
def factorial(numIn):
    if numIn > 1:
        return numIn * factorial(numIn-1)
    else:
        return 1
    
ans = factorial(5)
print(ans)

# Q2
myList = [85,24,63,45,17,31,96,50]
key = 17
location = 0
for index in range(len(myList)):
    if myList[index] == key:
        location = index

print("Key found at ", location)