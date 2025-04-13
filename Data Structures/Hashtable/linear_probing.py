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
    
    def probing_sequence(self, hashKey):
        #* range is used to unpack range object into a list, otherwise it will raise type error
        probRange = [*range(hashKey,len(self.arr))] + [*range(0, hashKey)]
        # print(probRange)
        return probRange
    
    def __setitem__(self, key, value):
        hashKey = h.get_hashKey(key)
        prob_range = h.probing_sequence(hashKey)
        inserted = 0
        for i in prob_range:
            #Inserting new key value pairs
            if self.arr[i] == None:
                self.arr[i] = (key, value)
                inserted = 1
                break
            else:
                #Updating value of existing key
                if self.arr[i][0] == key:
                    self.arr[i] = (key, value)
                    inserted = 1
                    break

                #Collision handling
                else:
                    continue
        
        if inserted == 0:
            raise Exception("No space left to add this new key value pair into this hashtable", key)


    def __getitem__(self, key):
        hashKey = h.get_hashKey(key)
        prob_range = h.probing_sequence(hashKey)

        for i in prob_range:
            if self.arr[i] != None:
                if key == self.arr[i][0]:
                    return self.arr[i][1]
            
            else:
                return self.arr[i]
            

    def __delitem__(self, key):
        hashKey = h.get_hashKey(key)
        prob_range = h.probing_sequence(hashKey)
        
        for i in prob_range:
            if self.arr[i] != None:
                if key == self.arr[i][0]:
                    self.arr[i] = None
            
    

        
    

h = Hashtable()
h["march"] = 100
h["march"] = 200
h["april"] = 300
h["may"] = 500
h["june"] = 700
h["afrah"] = 1000
h["azeera"] = 320
h["afrah"] = 2000
h["siva"] = 5000
h["hello"] = 7000
h["kish"] = 8000
h["babe"] = 9000
# h["element"] = 7800

print(h["babe"])
print(h["afrah"])
print(h["hey"])
del h["babe"]
h["element"] = 7800
print(h.arr)