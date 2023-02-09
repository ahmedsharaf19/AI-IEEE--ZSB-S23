def sort (unList) :
    return sorted(unList)

def first_last_apperance (sList,target) :
    return sList.index(target) , (len(unList)-1) - (unList[::-1].index(target)) 


unList =  input().split()
target=input()
unList = sort(unList)
first , last = first_last_apperance(unList,target)
print(first,last)