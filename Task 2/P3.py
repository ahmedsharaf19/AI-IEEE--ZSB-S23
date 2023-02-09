def max_subarray(array): 
    array_sorted=sorted(array)
    reversed_array=array_sorted[::-1]
    sub_max=[reversed_array[0]]
    result=reversed_array[0]
    for i in range(1,len(reversed_array)):
        buffer=result+ reversed_array[i]
        if(result <= buffer or len(sub_max)== 1):
            sub_max.append(reversed_array[i])
            result=buffer
        else:
            break
    
    return sub_max,result

def smallest_sum(array): 
    array_sorted=sorted(array)
    sub_mim=[array_sorted[0]]
    result=array_sorted[0]
    for i in range(1,len(array_sorted)):
        buffer=result+ array_sorted[i]
        if(result >= buffer or len(sub_mim)== 1):
            sub_mim.append(array_sorted[i])
            result=buffer
        else:
            break
    return sub_mim,result



array= [5 ,4 ,-1, 7, 8]

max_ar,result_max_sub=max_subarray(array)
print(f"{max_ar} ({result_max_sub})")


#https://www.youtube.com/watch?v=3GD-3UZGsVI
#https://www.youtube.com/watch?v=5WZl3MMT0Eg
#https://www.youtube.com/watch?v=ohHWQf1HDfU&t=295s

min_ar,result_min_sub=smallest_sum(array)
print(f"{min_ar} ({result_min_sub})")
