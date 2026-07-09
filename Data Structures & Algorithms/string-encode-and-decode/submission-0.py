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

            hashtag_index  =  s.find("#", i)

            length = int(s[i:hashtag_index])

            wordstart = hashtag_index + 1

            wordend = wordstart + length

            result.append(s[wordstart:wordend])
            i = wordend

        return result






