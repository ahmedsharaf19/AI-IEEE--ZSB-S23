x = list(input().split())
myList = []
for n in x :
    myList.append(int(n))

myList.sort()
print(myList[-2])
print(myList[1])