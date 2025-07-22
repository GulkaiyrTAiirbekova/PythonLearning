class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = []
        resLen = 0
        for key, val in enumerate(s):
            l, r = key, key
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = (r - l) + 1
                l -= 1
                r += 1
            l, r = key, key + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = (r - l) + 1
                l -= 1
                r += 1

        return res
