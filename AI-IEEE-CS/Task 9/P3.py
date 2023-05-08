class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # set to store unique email
        name = set()
        # loop for each element in emails
        for local in emails :
            # replace each '.' to '' from beginning to "@" and concaing from "@" to end
            temp = local[:local.find("@")].replace('.','') + local[local.find("@"):]
            # find index char "+" if found
            indx = temp.find("+")
            # check found or not
            if indx != -1 :
                # if found remove each character to "@"
                temp = temp[:indx] + local[local.find("@"):]
            # add converted email to set
            name.add(temp)
        # retuen len of set == number of different addresses that actually receive mails 
        return len(name)
