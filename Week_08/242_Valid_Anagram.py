class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

## 暴力求解 sort 把字符重新排序然后看对不对 o(nlogN)
## hash map 统计每个字符的频次


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