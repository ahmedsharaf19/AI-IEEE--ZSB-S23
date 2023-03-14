class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Conver String to alpha
        s = list(filter(lambda x : x.isalnum() ,s.strip().lower()))
        # Flag Check Palindrome Or Not
        flag = True if s[:] == s[::-1] else False
        # return flag
        return flag