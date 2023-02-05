x = [[[10,7,50],[16,20,16],[50,7,10]]]
flag = True
for i in range(len(x)) :
    for j in range(len(x)):
        if x[i][j] != x[j][i] : 
            flag= False
            break
    if flag == False : break

print(flag)