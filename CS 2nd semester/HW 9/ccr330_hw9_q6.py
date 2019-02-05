import string
class InvertedFile:
    def __init__(self,file_name):
        self.d = list(open(file_name).read().split())
        self.n = [word.strip(string.punctuation) for word in self.d]
        self.f = [word.lower() for word in self.n]
    def indices(self,word):
        if word not in self.f:
            return []
        else:
            indices = [ind for ind,elem in enumerate(self.f) if elem == word]
            return indices
            
            
        
        
def main():
    file = InvertedFile("row your boat.txt")
    print(file.indices('the'))
main()