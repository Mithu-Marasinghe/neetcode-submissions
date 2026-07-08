class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for val in strs:
            count = [0] * 26
            for c in val:
                count[ord(c) - ord('a')] += 1
            tuple_count = tuple(count)
            hash_map[tuple_count].append(val)
        return(list(hash_map.values()))