from oop1 import Stacks
def inputexp():
    pass
def validate(expression1):
    pass

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
    return s.Top()

def validate(expression1):
    j=0
    k=0
    for i in expression1:
        if i.isdigit() == True:
            j = j+1
        elif i== '+' or i== '-' or i== '*' or i== '/':
            k = k+1
        else:
            print(f"Invalid character at {expression1.index(i)}")
            return 3

    if j == k+1:
        return postfixexp(expression1)
    else:
        print("Invalid Expression")
        return 4

def inputexp():
    n = int(input("Enter the length of the postfix expression: "))
    expression1 = []
    for i in range(1,n+1):
        expression1.append(input(f"Enter the {i}^th element: "))

    return validate(expression1)
print(f"{inputexp()}")