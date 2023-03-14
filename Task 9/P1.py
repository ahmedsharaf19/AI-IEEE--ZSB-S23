class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Variable Store The Max Number From Right
        temp_max = -1
        # Number Of Element In Array
        number_element = len(arr)
        # Loop To Each Elemnet 
        for i in range(number_element-1,-1,-1) :
            # Compare Between Tow Element And Store Maximum In Variable Maximum 
            maximum = max(temp_max,arr[i])
            # Store temp_max from right array
            arr[i] = temp_max
            # Store maximum element in temp_arr
            temp_max = maximum
        # return arr
        return arr
    

    