import random
import unsorted_map
Item = unsorted_map.UnsortedArrayMap.Item
class ChainingHashTableMap:
    def __init__(self, N=64, p=6460101079):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash_function(self, k):
        int_code_of_k = hash(k)
        ind = ((self.a*int_code_of_k + self.b) % self.p) % self.N
        return ind

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if (curr_bucket is None):
            raise KeyError(str(key) + " not found")
        elif (type(curr_bucket) is Item):
            return curr_bucket.value
        else:
            return curr_bucket[j]

    def __setitem__(self, key, value):
        j = self.hash_function(key)  
        if(self.table[j] is None):
            self.table[j] = Item(key,value)
            old_size = 0
            new_size = 1
        elif (type(self.table[j]) is Item):
            temp = self.table[j]
            self.table[j] = unsorted_map.UnsortedArrayMap()
            self.table[j][temp.key] = temp.value
            self.table[j][key] = value
            old_size = 1
            new_size = 2
        else:
            old_size = len(self.table[j])            
            self.table[j][key] = value            
            new_size = len(self.table[j])
        if(new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if(curr_bucket is None):
            raise KeyError(str(key) + " not found")
        elif(type(curr_bucket) is Item):
            self.table[j] = None
        elif(len(curr_bucket) == 2):
            del curr_bucket[key]
            for item in curr_bucket:
                self.table[j] = Item(item,curr_bucket[item])
        else:
            del curr_bucket[key]
        self.n -= 1
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None and type(curr_bucket) is not Item):
                for key in curr_bucket:
                    yield key
            if (type(curr_bucket) is Item):
                yield curr_bucket
                
    def rehash(self, new_size):
        old_data = []
        for key in self:
            value = self[key]
            old_data.append((key, value))
        self.table = [None] * new_size
        self.N = new_size
        self.n = 0
        for (key, value) in old_data:
            self[key] = value
