x = list(input().split())
numRotate = int(input())
myList =[]
for n in x :
    myList.append(int(n))

n = len(myList) - numRotate
temp = myList[:n]

for ind in range(numRotate) :
    temp.insert(0,myList[-1])
    myList.pop(-1)
    

myList = temp
print(myList)