x = list(input().split())
myList1 = []
myList2 = []
for n in x :
    if len(n) % 2 == 0:
        myList1.append(n[:int(len(n)/2)])
        myList2.append(n[int(len(n)/2):])
    else :
        myList1.append(n[:int(len(n)/2) +1])
        myList2.append(n[int(len(n)/2) +1:])

print(myList1)
print(myList2)