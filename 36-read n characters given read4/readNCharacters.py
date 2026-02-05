from typing import List


class FileReader:
    def __init__(self, content):
        self.content = content
        self.pointer = 0  # file pointer

    def read4(self, buf4):
        count = 0
        while count < 4 and self.pointer < len(self.content):
            buf4[count] = self.content[self.pointer]
            self.pointer += 1
            count += 1
        return count




def read(bufs : List[str] , n : int ) -> int :
    
    total = 0
    tmp = [''] * 4
    
    reader = FileReader("abcdefghigklmnop")
    
    while total < n :
        
        count = reader.read4(tmp)
        
        for i in range(count):
            if total == n: break
            bufs[total] = tmp[i]
            total += 1
        
        if count < 4:
            break
            
    return total
        