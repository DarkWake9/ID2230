from oop1 import Stacks
expression1 = ['2','23','+','11','12','13','-','*','-'] #Result = 36
# Read the input tokens. Create an empty stack S.
#2. For each token x, do:
#If x is a number, Push(S,x).
#Else if x is an operator, do:
#Set a=Pop(S).
#Set b=Pop(S).
#Push(S,bxa).
#3. Return Top(S).
def postfixexp(expression1):
    s = Stacks()
    for x in expression1:
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
        else:
            print(f"Invalid character at {s.array.index(x)}")
            #    return 3
    #print(f"{s.Top()}")    
    return s.Top()
print(f"{postfixexp(expression1)}")