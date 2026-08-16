class Solution:
    def isPalindrome(self, s: str) -> bool:
        sr = [c.lower() for c in s if c != ' ' and c.isalnum() ]
        l = int(len(sr)/2)
        for x in range(0,l):
            print(sr[x])
            print(sr[(len(sr)-1)-x])
            if sr[x] != sr[(len(sr)-1)-x]:
                return False
        print(sr)
        return True
        