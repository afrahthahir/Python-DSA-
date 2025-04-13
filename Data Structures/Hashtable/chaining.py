class Hashtable:
    def __init__(self):
        self.MAX = 10
        #Implementing chaining in hashmap so at each index of the list(Hashmap),
        #there is a list or linkedlist with key value pairs Ex: ("march",100)->("june",200) each element is a tuple
        self.arr = [[] for i in range(self.MAX)]


    # Get hash key from using a hash function 
    def get_hashKey(self,key):
        hashKey = 0
        for char in key:
            hashKey += ord(char)
        # print(hashKey % self.MAX)
        return hashKey % self.MAX
    

    #setting values to key
    def __setitem__(self,key,value):
        haskKey = h.get_hashKey(key)
        # print(haskKey)
        # print(len(self.arr[haskKey]))
        updated = 0
        #To update value to an existing key
        if len(self.arr[haskKey]) >= 1:  
            for index, (k, v) in enumerate(self.arr[haskKey]):
                if k == key:
                    self.arr[haskKey][index] = (k, value)
                    updated = 1
                    break
                    
        #when there is no exisitng key
        if updated == 0:
            self.arr[haskKey].append((key,value))
        
    
    #getting values of the key
    def __getitem__(self,key):
        hashKey = h.get_hashKey(key)
        for i, (k,v) in enumerate(self.arr[hashKey]):
            if k == key:
                return v
    
    #deleting values of a key 
    def __delitem__(self,key):
        hashKey = h.get_hashKey(key)
        for i, (k,v) in enumerate(self.arr[hashKey]):
            if k == key:
                self.arr[hashKey][i] = []
    

h = Hashtable()
h["march"] = 100
h["april"] = 300
h["may"] = 500
h["june"] = 700
h["july"] = 900
h["july"] = 1000

h["july"] = 9000

h["afrah"] = 1000
h["afrah"] = 800
h["siva"] = 780
h["azeera"] = 990
print(h["july"])
print(h["siva"])
print(h["azeera"])
print(h["afrah"])

del h["june"]
del h["afrah"]

print(h.arr)