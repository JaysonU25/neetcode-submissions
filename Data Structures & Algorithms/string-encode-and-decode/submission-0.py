import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        s: str = ""
        for srs in strs:
            print(srs)
            s = s + srs + "<JAYSON_SPLIT>"

        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        return s.split("<JAYSON_SPLIT>") [:-1]       
