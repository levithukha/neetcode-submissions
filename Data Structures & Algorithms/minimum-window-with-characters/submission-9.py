class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        target = {}
        window = {}

        for c in t:
            target[c] = target.get(c, 0) + 1 

        matched = 0
        required = len(target)

        left = 0
        result = [-1, -1]
        smallest = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                matched += 1

            while matched == required:

                if right - left + 1 < smallest:
                    smallest = right - left + 1 
                    result = [left, right]

                left_char = s[left]

                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    matched -= 1

                left += 1

        if smallest == float("inf"):
            return ""

                
        left, right = result
        return s[left:right + 1]





