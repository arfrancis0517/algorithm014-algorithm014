class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        temp_dict={}
        for temp_str in strs:
            sort_str = self.HashMapFunc(temp_str)
            if sort_str in temp_dict:
                temp_dict[sort_str].append(temp_str)
            else:
                temp_dict[sort_str]=[temp_str]
        return list(temp_dict.values())


    def HashMapFunc(self, temp_str):
        return ''.join(sorted(list(temp_str)))