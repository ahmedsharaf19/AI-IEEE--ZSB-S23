dic = {}
list1=[]
for n in input().split(",") :
    list1 += n.split(":")

list1_key = list1[::2]
list1_value = list1[1::2]

for key in list1_key:
    for value in list1_value:
        dic[key] = value
        list1_value.remove(value)
        break
list2=[]
for n in input().split(",") :
    list2 += n.split(":")

list2_key = list2[::2]
list2_value = list2[1::2]
for key in list2_key:
    for value in list2_value:
        dic[key] = value
        list2_value.remove(value)
        break
print(dic)