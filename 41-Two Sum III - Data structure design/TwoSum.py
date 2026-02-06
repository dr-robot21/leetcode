class TwoSum :
    def __init__(self):
        self.data = []
    
    def add(self ,x : int ) :
         self.data.append(x)
    
    
    def find(self , x : int ) -> bool :
        s = set()
        for num in self.data:
            y = x - num
            if y in s:
                return True
            s.add(num)
            
        return False
            
[1,3,5,7] = 4