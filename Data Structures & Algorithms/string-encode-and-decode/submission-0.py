class Solution:

    def encode(self, strs: List[str]) -> str:
        lst = []

        for s in strs:
            new_len = len(s)
            new_str = str(new_len) + "#" + s

            lst.append(new_str)

        new_str = "".join(lst)

        return new_str
        
    def decode(self, s: str) -> List[str]:
        new_lst = []

        idx = 0

        while (idx < len(s)):
            j = s.index("#", idx)

            l = int(s[idx:j])

            new_lst.append(s[j + 1:j + 1 + l])

            idx = j + 1 + l

        return new_lst
