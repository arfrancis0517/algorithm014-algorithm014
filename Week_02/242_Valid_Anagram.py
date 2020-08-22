class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s) != len(t):
            return False
        else:
            cnt_s = Counter()
            cnt_t = Counter()
            for letter in s:
                cnt_s[letter]+=1
            for letter in t:
                cnt_t[letter]+=1
            return cnt_s == cnt_t