class CombinationIterator:
    def __init__(self, characters: str, l: int):
        self.combos = list(itertools.combinations(characters ,l))  
        self.index=0    
        self.length = len(self.combos)  

    def next(self) -> str:
        self.index+=1 
        return ''.join(self.combos[self.index-1]) 

    def hasNext(self) -> bool:
        return self.index < self.length  