学习笔记

# Atoi 代码示例

# Python

class Solution(object):
    def myAtoi(self, s):
        if len(s) == 0 : return 0
        ls = list(s.strip())
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))

# KMP算法
    def kmp(str1, str2):
        if str1 == None or str2 == None or len(str1) < len(str2):
            return False
        index = 0                           # index为str2对应于每次开始的位置
        len1, len2 = len(str1), len(str2)
        moveTable = matchTable(list(str2))
        pAppear = []
        while index <= len1 - len2:
            tmpIndex = 0                    # tmpIndex为str2中字符走到的位置
            while tmpIndex < len2 and str1[index+tmpIndex] == str2[tmpIndex]:
                tmpIndex += 1
            if tmpIndex == len2:
                pAppear.append(index)
                index += len2
                continue
            elif tmpIndex > 0:
                index += tmpIndex - moveTable[tmpIndex-1]
            else:
                index += 1
        return pAppear if pAppear else False

    # 生成KMP匹配表, 该表和next表不一样

    def matchTable(aList):
        length = len(aList)
        table = [0]*length
        index = 1
        while index < length:
            sameLen = 0
            while aList[:sameLen+1] == aList[index:index+sameLen+1]:
                sameLen += 1
                table[index+sameLen-1] = sameLen
            if sameLen != 0:
                index += sameLen
            else:
                index += 1
        return table

# BoyerMoore算法
    
    def BoyerMoore(original, pattern):
        if original == None or pattern == None or len(original) < len(pattern):
            return None
        len1, len2 = len(original), len(pattern)
        pAppear = []
        # 查找一个字符使用蛮力法即可
        if len2 == 1:
            for i in range(len1):
                if original[i] == pattern[0]:
                    pAppear.append(i)
        else:
            badTable = badCharTable(pattern)
            goodTable = goodSuffixTable(pattern)
            index = len2 - 1
            while index < len1:
                indexOfP = len2 - 1
                while index < len1 and pattern[indexOfP] == original[index]:
                    if indexOfP == 0:
                        pAppear.append(index)
                        index += len2 + 1
                        indexOfP += 1
                        continue
                    index -= 1
                    indexOfP -= 1
                if index < len1:
                    index += max(goodTable[len2 - 1 - indexOfP], badTable[original[index]])
        return pAppear if pAppear else False
    '''
    生成一个坏字符表, 移动距离分为两种
    字符不在模式中, 移动的长度为模式的长度;
    字符在模式中,移动的长度为模式中最右边对应待检测字符对应的模式中存在的此字符到最后一个字符的距离
    对于BARBER，除了E,B,R,A的单元格分别为1，2，3，4之外，所有字符移动的单元格均为6
    '''
    def badCharTable(pattern):
        table = {}
        length = len(pattern)
        alphaBet = list(map(chr, range(32, 127)))   # 利用map生成一个原始移动表, 对应字符为从SPACE到~, 使用UTF-8对应表
        for i in alphaBet:
            table[i] = length
        # 更改pattern中存在字符的对应移动距离
        for j in range(length-1):
            table[pattern[j]] = length - 1 - j
        return table
    
    '''
    生成一个好后缀表
    '''
    def goodSuffixTable(pattern):
        length = len(pattern)
        tabel = [0] * length
        lastPrefixPosition, i = len(pattern), length - 1
        while i >= 0:
            if isPrefix(pattern, i):
                lastPrefixPosition = i
            tabel[length - 1 - i] = lastPrefixPosition - i + length - 1
            i -= 1
        for i in range(length-1):
            slen = suffixLength(pattern, i)
            tabel[slen] = length - 1 - i + slen
        return tabel
    '''
    判断模式后面几个字符是否等于模式前面相应长度的字符
    '''
    def isPrefix(pattern, p):
        length, j = len(pattern), 0
        for i in range(p, length):
            if pattern[i] != pattern[j]:
                return False
            j += 1
        return True
    '''
    判断前缀以及后缀的重复长度
    '''
    def suffixLength(pattern, p):
        length, samLen = len(pattern), 0
        i, j = p, length-1
        while i >= 0 and pattern[i] == pattern[j]:
            samLen += 1
            i -= 1
            j -= 1
        return samLen
    print(BoyerMoore('aaaaa', 'aa'))

# Sunday算法

    def Sunday(str1, str2):
        if str1 == None or str2 == None or len(str1) < len(str2):
            return None
        len1, len2 = len(str1), len(str2)
        pAppear, moveDict = [], matchDict(list(str2))
        indexStr1 = 0
        while indexStr1 <= len1 - len2:
            indexStr2 = 0
            while indexStr2 < len2 and str1[indexStr1 + indexStr2] == str2[indexStr2]:
                indexStr2 += 1
            if indexStr2 == len2:
                pAppear.append(indexStr1)
                indexStr1 += len2
                continue
            if indexStr1 + len2 >= len1:
                break
            elif str1[indexStr1+len2] not in moveDict.keys():
                indexStr1 += len2 + 1
            else:
                indexStr1 += moveDict[str1[indexStr1+len2]]
        return pAppear if pAppear else False
    
    def matchDict(aList):
        moveDict = {}
        length = len(aList)
        for i in range(length-1, -1, -1):
            if aList[i] not in moveDict.keys():
                moveDict[aList[i]] = length - i
        return moveDict


# 字符串匹配暴力法代码示例

# Python

    def forceSearch(txt, pat):
        n, m = len(txt), len(pat)
        for i in range(n-m+1):
            for j in range(m):
                if txt[i+j] != pat[j]:
                    break
                if j == m:
                    return i
        return -1 

# Rabin-Karp 代码示例

    class Solution:
        def strStr(self, haystack: str, needle: str) -> int:
            d = 256
            q = 9997
            n = len(haystack)
            m = len(needle)
            h = pow(d,m-1)%q
            p = 0
            t = 0
            if m > n:
                return -1
            for i in range(m): # preprocessing
                p = (d*p+ord(needle[i]))%q
                t = (d*t+ord(haystack[i]))%q
            for s in range(n-m+1): # note the +1
                if p == t: # check character by character
                    match = True
                    for i in range(m):
                        if needle[i] != haystack[s+i]:
                            match = False
                            break
                    if match:
                        return s
                if s < n-m:
                    t = (t-h*ord(haystack[s]))%q
                    t = (t*d+ord(haystack[s+m]))%q
                    t = (t+q)%q
            return -1

