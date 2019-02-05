class Integer(object) :
    def __init__(self, num_str) :
        self.num = int(num_str)
        
    def __add__(self, other) :
        if type(other) == Integer :
            return Integer(self.num + other.num)
            
    def __str__(self) :
        return str(self.num)
        
    def __repr__(self):         
        return str(self) 
        
	