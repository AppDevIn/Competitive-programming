class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        raw = ''.join(c for c in s if c != "-")


        index = len(raw)
        reformatted = ""
        while index > k:
            reformatted = "-" + raw[index-k:index] + reformatted
            index -= k
        
        return (raw[0:index] + reformatted).upper()
