class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            temp = word.split(separator)
            for item in temp:
                if item!="":
                    res.append(item)
        return res
        