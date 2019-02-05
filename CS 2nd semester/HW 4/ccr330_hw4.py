#Claudia Rodriguez Hw 4 

#Question 1 - Rearrange negatives in front of positives
def split_by_sign(lst, low, high):
    new_lst = lst[low:]
    while new_lst != []:
        max = lst.pop(high)
        if lst[max]>0:
            return
        else:
            return split_by_sign(lst,low,high-1)


#Question 2 - make a list of all combos
def permutation(lst):
   if len(lst) == 1:
     return [lst]
   new_list = [] 
   for elem in lst:
     remaining_elements = [x for x in lst if x != elem]
     sublist = permutation(remaining_elements) 
     for num in sublist:
       new_list.append([elem] + num)

   return new_list
   
#Question 3 - add pop and insert to MyList
class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for ind in range(self.n):
            new_array[ind] = self.data[ind]
        self.data = new_array
        self.capacity = new_size

    def extend(self, other):
        for elem in other:
            self.append(elem)

    def __getitem__(self, ind):
        if not(0 <= ind <= self.n - 1):
            raise IndexError('MyList index is out of range')
        return self.data[ind]

    def __setitem__(self, ind, val):
        if not(0 <= ind <= self.n - 1):
            raise IndexError('MyList index is out of range')
        self.data[ind] = val

    def __str__(self):
        return (",self.data,")

    def __repr__(self):
        return str(self);

    def __add__(self, other):
        my_list3 = self.data + other.data;
        return Day(my_list3);
    def __iadd__(self, other):
        self.data += other.data;
        return self;
    def insert(self, index, val):
        return self.data[:index] + [val] + self.data[index:];
    def pop(self):
        return self.data.pop();
        
        
#Question 4A - create a list with just the repeated values
def find_duplicates(lst):
    n = 1
    new_lst = []
    for i in lst:
        if i in lst[n:]:
            new_lst.append(i)
        n+=1
    return new_lst
            
#Question 5b -  removes first occurence of value in list
def remove_all(lst, value):
    end = False
    while (end == False):
        try:
            lst.remove(value)
        except ValueError:
            end = True
            
def remove_all2(lst, value):
    for elem in lst:
        if elem == value:
            lst.remove(value)
    return lst
    
       