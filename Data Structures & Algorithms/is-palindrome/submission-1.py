class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=""
        for i in s.lower():
            if i.isalnum():
                p=p+i
        return p==p[::-1]