from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        # 문자를 정렬한 값을 key값으로 안에 value를 넣음.
        for s in strs:
            str_dict[''.join(sorted(list(s)))].append(s)
        return list(str_dict.values())
            