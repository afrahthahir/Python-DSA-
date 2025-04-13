#Write a function in python that can reverse a string using stack data structure.
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"


from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push_string(self, string):
       for char in string:
           self.stack.append(char)
    #    print(self.stack)

    def reverse_string(self, string):
        s.push_string(string)
        newString = ""
        while len(self.stack) > 0:
            last = self.stack.pop()
            # print(last)
            newString += last
        print(newString)
        
            

s = Stack()
# s.push_string()
s.reverse_string("We will conquere COVID-19")