x = input().split(",")
list =[]
for n in x :
    list.append(n.split(":"))

x = input().split(",")
for n in x :
    list.append(n.split(":"))

list = dict(list)
dict = {}
for main_key , main_value in list.items() :
    dict.setdefault(main_key,int(main_value)) 

print(dict)