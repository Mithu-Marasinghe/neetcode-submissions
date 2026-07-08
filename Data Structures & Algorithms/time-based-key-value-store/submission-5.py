class TimeMap:
    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        key_list = self.mp.get(key, [(-1, "")])
        l = 0
        r = len(key_list) - 1

        while (l < r):
            mid = math.ceil((l + r) / 2)
            mid_value = key_list[mid][0]

            if (timestamp < mid_value):
                r = mid - 1
            else:
                l = mid

        if (key_list[l][0] <= timestamp):
            return key_list[l][1]
        return ""
                
        
