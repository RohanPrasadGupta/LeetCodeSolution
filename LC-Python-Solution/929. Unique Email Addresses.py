class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        eSet = set()

        for email in emails:
            name,domain = email.split("@")

            atIndex = name.find("+")
            if atIndex !=-1:
                name = name[:atIndex]
            
            name = name.replace(".","")
            eSet.add(name+"@"+domain)
        
        return len(eSet)




        