class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]


    # Get hash key from using a hash function 
    def get_hashKey(self,key):
        hashKey = 0
        for char in key:
            hashKey += ord(char)
        return hashKey % self.MAX
    

    #setting values to key
    def __setitem__(self,key,value):
        haskKey = h.get_hashKey(key)
        self.arr[haskKey] = value
    
    #getting values of the key
    def __getitem__(self,key):
        hashKey = h.get_hashKey(key)
        return self.arr[hashKey]
    
    #deleting values of a key 
    def __delitem__(self,key):
        hashkey = h.get_hashKey(key)
        self.arr[hashkey] = None

    
    

h = Hashtable()
h["march"] = 100
h["april"] = 300
h["may"] = 500
h["june"] = 700

print(h["march"])

print(h.arr)
del h["june"]
print(h.arr)