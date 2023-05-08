"""
    Modulue Containe 5 Function To Implement 5 number Summary And Virance And Standard_Derviation
    Task - 4
    Coded By : Ahmed Sharaf
    Date : 19 / 2 / 2023
    Note : Not Import Any library
"""
def check_number_length (lst) :
    """
    Function To Check The Length Of List ( Odd Or Even)
    Parameter : List Nedded To Check
    Return True If Length Even Else False
    """
    return True if len(lst) % 2 == 0 else False

def find_quartile(lst) :
    """
    Function To Find The Quartile
    Parameter : List Contain Of Element
    Return Quartile
    """
    return (lst[len(lst) // 2] + lst[(len(lst) // 2) - 1]) / 2 if check_number_length(lst) else  lst[len(lst) // 2]
    
def five_number_summary (lst) :
    """
    Function To Determin 5 number summary ( min , Q1 , Q2 , Q2 , max)
    Parameter : List 
    Return List Conatin Five Number Summary
    """
    lst = sorted(lst)
    maximum = lst[-1]
    minimum = lst[0]
    q1,q2,q3 = 0 , 0 , 0
    middle_elemnt = len(lst) // 2
    flag_even = check_number_length(lst)
    if  flag_even :
        q2 = (lst[middle_elemnt] + lst[middle_elemnt - 1]) / 2
        q1 = find_quartile(lst[:middle_elemnt])
        q3 = find_quartile(lst[middle_elemnt:])
    else :
        q2 = lst[middle_elemnt]
        q1 = find_quartile(lst[:middle_elemnt])
        q3 = find_quartile(lst[middle_elemnt+1:])

    return minimum,q1,q2,q3,maximum

def range_iqr(lst) :
    """
    Function To Determine The Range ( Max  - Min) And Interquartile Range ( Q3 - Q1 )
    Parameter : List 
    Return Range And IQR
    """
    range = lst[-1] - lst[0]
    iqr = lst[-2] - lst[1]

    return range , iqr

def standard_derivation(lst) :
    """
    Function To Determine Vriance And Standard Derivation
    Parameter : List 
    Return Vriance And Standard Derivation
    """
    mean = sum(lst) / len(lst)
    square_summition = 0
    for i in lst :
        square_summition += ((i-mean) ** 2)
    vriance  = square_summition / len(lst)
    standard_derivation_number = (vriance) ** (1/2)
    return vriance , standard_derivation_number


# Try And Except To Handle Any Error
try :
    lst = [float(i) for i in input().split()]
except ValueError :  # If Users Enter Value Not Equal Number
    print("Please Enter Valid Number !")
except KeyboardInterrupt :   # If Users Neded To Exit The Program 
    print("Good Bye!")
except :
    print("Please Check Your Input!")
else :   # Excute If No Error
    new_lst_five_number_symmary = five_number_summary(lst)
    new_lst_obtained_r_iqr = range_iqr(new_lst_five_number_symmary)
    new_standard_deviation = standard_derivation(lst)
    print(f"min : {new_lst_five_number_symmary[0]}")
    print(f"Q1 : {new_lst_five_number_symmary[1]}")
    print(f"Q2 : {new_lst_five_number_symmary[2]}")
    print(f"Q3 : {new_lst_five_number_symmary[3]}")
    print(f"max : {new_lst_five_number_symmary[4]}")
    print(f"range : {new_lst_obtained_r_iqr[0]}")
    print(f"IQR : {new_lst_obtained_r_iqr[1]}")
    print(f"Variance : {new_standard_deviation[0]:0.2f}")
    print(f"Standard deviation : {new_standard_deviation[1]:0.3f}")




