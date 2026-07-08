class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        while len(strs) > 0:
            objects_to_remove = []
            new_set = []
            first_value = strs[0]
            string1Map = self.calculateStringMap(first_value)

            objects_to_remove.append(first_value)

            for i in range(1, len(strs)):
                if self.isAnagram(strs[i], string1Map):
                    objects_to_remove.append(strs[i])
            
            for val in (objects_to_remove):
                new_set.append(val)

            results.append(new_set)

            for i in objects_to_remove:
                strs.remove(i)

        return results 

    def isAnagram(self, string2, string1Map):
        string2Map = self.calculateStringMap(string2)
        return string1Map == string2Map

    def calculateStringMap(self, first_value):
        result = {}
        for char in first_value:
            result[char] = result.get(char, 0) + 1
        
        return result