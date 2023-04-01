class BinaryTriangle:
    def __init__(self, n):
        self.levels = []
        for i in range(1, n+1):
            self.levels.append([1]*i)
            
    def __str__(self):
        res = ''
        for i in range(len(self.levels)):
            res += ' '.join(str(val) for val in self.levels[i])
            res += '\n'
        return res
            
                 
bt = BinaryTriangle(6)
print(bt)  # prints the initial triangle
