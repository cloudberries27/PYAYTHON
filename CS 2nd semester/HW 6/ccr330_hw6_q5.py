class CompactString:     
    def __init__(self, orig_str):
        self.compact = orig_str         
                 
    def __add__(self, other): 
        if type(other) == CompactString :
            return CompactString(self.compact + other.compact)        
    
    def __lt__(self, other): 
        return CompactString(self.compact < other.compact)        
             
    def __le__(self, other):
        return CompactString(self.compact <= other.compact)           
                 
    def __gt__(self, other):    
        return CompactString(self.compact > other.compact)  
    
    def __ge__(self, other): 
        return CompactString(self.compact >= other.compact)          
           
    def __str__(self):  
        return str(self.compact)  
         
    def __repr__(self):        
        return str(self) 
 

