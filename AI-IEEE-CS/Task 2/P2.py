x = input().split() 
x = [int(i) for i in x]
list_temp = list(filter(lambda test : test % 2 == 0 , x))
print(len(list_temp))