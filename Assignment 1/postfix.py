from oop1 import Stacks
expression1 = ['2','23','+','11','12','13','-','*','-', '35']

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
            print(f"Invalid character at {s.array.index(x)}")
            return 3

    if j == k+1:
        return postfixexp(expression1)
    else:
        print("Invalid Expression")
        return 4
print(f"{validate(expression1)}")