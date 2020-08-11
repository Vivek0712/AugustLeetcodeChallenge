class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if not citations:
            return 0
        
        citations.sort(reverse = True)
        
        for index,value in enumerate(citations):
            if index>=value:
                return index
        return len(citations)
                