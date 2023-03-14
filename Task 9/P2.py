class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Conver String to alpha
        s = list(filter(lambda x : x.isalnum() ,s.strip().lower()))
        # flag True if s is palindrom else false
        flag =  True
        for i in range(len(s)) :
            # if end element not equal first element "Not Palindrom"
            if s[i] != s[-(i+1)] :
                flag = False
                break
        # return flag
        return flag
