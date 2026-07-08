class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''.join(f"{len(s)}#{s}" for s in strs)
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            # print(i, s[i], result)
            val = s[i]
            i+=1
            str_len = f'{val}'
            while (s[i] != '#'):
                str_len += s[i]
                i += 1

            num = int(str_len)
            partial_result = ''
            for count in range(i + 1, i + 1 + num):
                partial_result += s[count]
            result.append(partial_result)
            i += 1 + num
        return result
