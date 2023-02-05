x = input()
flag = True
for i in range(len(x)) :
    if x[i] != x[-i-1] : 
        flag = False
        break

print(flag)