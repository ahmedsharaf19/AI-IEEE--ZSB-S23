row , col = map(int,input().split())
colored  = ['C','M','Y']
isColored = False
for i in range(row) :
    element_row = input().split()
    for element in element_row :
        if element in colored :
            isColored = True
            break

if isColored :
    print("#Color")
else :
    print("#Black&White")