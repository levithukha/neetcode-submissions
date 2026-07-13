class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result



    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):

            hashtag_index = s.find("#", i)

            number = int(s[i:hashtag_index])

            word_start = hashtag_index + 1
            word_end = word_start + number

            result.append(s[word_start:word_end])

            i = word_end

        return result