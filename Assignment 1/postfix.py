from oop1 import Stacks
expression1 = ['2','23','+','11','12','13','-','*','-']

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
            return 3  
    return s.Top()
print(f"{postfixexp(expression1)}")