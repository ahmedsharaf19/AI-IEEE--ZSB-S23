x = list(input("List Of Number : ").split())
tar = int(input("Target Number : ").strip())
myNum = []
for n in x :
    myNum.append(int(n))

ind = myNum.index(tar)
print(f"{ind-2}, {ind -1}")