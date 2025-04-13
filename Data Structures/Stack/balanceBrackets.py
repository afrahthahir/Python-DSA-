#Write a function in python that checks if paranthesis in the string are balanced or not.
#Possible parantheses are "{}',"()" or "[]". 

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def is_balanced(self,string):
        for char in string:
            # print("char",char)

            #Pushing only the opening brackets
            if char in "{([":
               print("push",char)
               self.stack.append(char)
            
            #Popping opening matched brackets when char is a closing matched bracket
            elif char in ")}]" and len(self.stack) != 0: 

                if char == "}" and self.stack[-1] == "{":
                    print("pop",char)
                    self.stack.pop()

                elif char == ")"  and self.stack[-1] == "(":
                    print("pop",char)
                    self.stack.pop()

                elif char == "]" and self.stack[-1] == "[":
                    print("pop",char)
                    self.stack.pop()

            #When there are closing brackets only, or closing brackets in middle of string, means unbalanced so return false
            elif char in ")]}" and len(self.stack) == 0: 
                print("None of the elements were pushed to stack")
                return False
                
        # Empty stack means, balanced else non balanced
        if len(self.stack) == 0:
            return True
        else:
            return False


s = Stack()
# result = s.is_balanced("({a+b})")
# result = s.is_balanced("))((a+b}{")
# result = s.is_balanced("((a+b))") 
# result = s.is_balanced("))")  
result = s.is_balanced("[a+b]*(x+2y)*{gg+kk}")
print(result)