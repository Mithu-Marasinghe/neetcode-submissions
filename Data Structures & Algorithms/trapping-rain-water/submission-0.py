class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixes = [0] * n
        suffixes = [0] * n
        total_area = 0

        # prefixes[0] = height[0]
        # Calculate Prefix Array
        for i in range(1, n):
            value = height[i - 1]
            if (value > prefixes[i - 1]):
                prefixes[i] = value
            else:
                prefixes[i] = prefixes[i - 1]

        # suffixes[-1] = height[-1]
        # Calculate Suffix Array
        for i in range(n - 2, -1, -1):
            value = height[i + 1]
            if (value > suffixes[i + 1]):
                suffixes[i] = value
            else:
                suffixes[i] = suffixes[i + 1]

        print(prefixes)
        print(suffixes)
        print('\n')
        
        for index, val in enumerate(height):
            min_height = min(prefixes[index], suffixes[index])
            print(f"Index: {index}, Prefix: {prefixes[index]}, Suffix: {suffixes[index]}")
            print(f"Min: {min_height}, Val: {val}")
            if (min_height > val):
                total_area += (min_height - val)

            print(total_area)
        return total_area

