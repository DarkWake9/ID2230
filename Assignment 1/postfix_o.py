#Program to Evaluate a given postfix expressions using Stacks
from Stack import Stacks

class PostFixExpr():

    def __init__(self):
        self.expression1 = []
        n = int(input("Enter the length of the postfix expression: "))
        for i in range(1,n+1):
            self.expression1.append(input(f"Enter the {i}^th element: "))

    #Evaluates the postfix expression
    def postfixexp(self):
        s = Stacks()
        for x in self.expression1:
            if x.isdigit() == True:
                s.Push(float(x))
            elif x == '+':
                a = s.Pop()
                b = s.Pop()
                s.Push(b+a)
            elif x == '-':
                a = s.Pop()
                b = s.Pop()
                s.Push(b-a)
            elif x == '*':
                a = s.Pop()
                b = s.Pop()
                s.Push(b*a)
            elif x == '/':
                a = s.Pop()
                b = s.Pop()
                s.Push(b/a)
        return s.Top()
    
    #Validates and evaluates the given postfix expression
    def validate(self):
        j=0
        k=0
        for i in self.expression1:
            if i.isdigit() == True:
                j = j+1
            elif i== '+' or i== '-' or i== '*' or i== '/':
                k = k+1
            else:
                print(f"Invalid character at {self.expression1.index(i)}")
                return 3

        if j == k+1:
            return self.postfixexp()
        else:
            print("Invalid Expression")
            return 4
    
#Driver Code
newexp = PostFixExpr()
print(newexp.validate())