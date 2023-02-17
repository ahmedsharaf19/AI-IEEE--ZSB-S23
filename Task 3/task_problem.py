"""
    This Module Using To Solve The Task - 3
    This Module Have Three Function : 
    1 - Function To Calculate Mean
    2 - Function To Calculate Median
    3 - Function To Calculate Mode
    Name : Ahmed Sharaf
    Date : 17 / 2 / 2023
"""
def mean(number) :
    """
        Function To Use Calculate Mean of Measuring OF Center
        parameter (number) => list of number
        return => average of number 
    """
    return sum(number) / len(number) # return Avg

def median(number) :
    """
        Function To Use Calculate Median of Measuring OF Center
        parameter (number) => list of number
        return => median of number 
    """
    number = sorted(number)  # Sort List To Calculate The Median Numner
    median = None
    med = len(list(number)) // 2 # To Get The Medille Number
    if len(list(number)) % 2 == 0 : #Equal Even claculate Median Using Avg Between To Medille Number
        median = (number[med] + number[med-1]) / 2
    else :   # If Odd The Median Equal To Medille Number Directly
        median = number[med] 
    return median

def mode(number) :
    """
        Function To Use Calculate Mode of Measuring OF Center
        parameter (number) => list of number
        return => Mode of number 
    """
    counte_max_number = 0  # To Calculate The Number Of Frquantly Number In lsit
    mode = number[0]       # The Number Of Frquantly in List
    for i in number :
        element = number.count(i)        # To Calculate Each Number How Many Repated
        if element > counte_max_number :  # check The Number Repated Grater Than The Previous Numner
            counte_max_number = element    # Store The Number Of Repated
            mode = i    # Store  The Number That Have The Max Count Of Repated
    return mode   # Return Mode
    
try :
    lst = [float(i) for i in input().split()]
    print(f"mean: {mean(lst):0.2f}") # Called Function mean To calculate Mean
    print(f"median: {median(lst)}")  # Called Function median To calculate Median
    print(f"mode: {mode(lst)}")      # Called Function Mode To Calculate Mode
except ValueError :                  # Exception Value Not Number
    print("Please Enter Valid Number")
except KeyboardInterrupt :           # Exception Exit Using Keyboard 
    print("Good By !")
    exit()
