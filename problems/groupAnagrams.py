from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for item in strs:
            key = tuple(sorted(item))
            if key in result:
                result[key].append(item)
            else:
                result[key]=[item]
        
        return list(result.values())

