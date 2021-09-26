from oop1 import Stacks
class PostFixExpr():
    def __init__(self, expression1):
        self.s = Stacks()
    def postfixexp(self, expression1):
    #s = Stacks()
        for x in expression1:
            if x.isdigit() == True:
                self.s.Push(float(x))
            elif x == '+':
                a = self.s.Pop()
                b =     self.s.Pop()
                self.s.Push(b+a)
            elif x == '-':
                a = self.s.Pop()
                b = self.s.Pop()
                self.s.Push(b-a)
            elif x == '*':
                a = self.s.Pop()
                b = self.s.Pop()
                self.s.Push(b*a)
            elif x == '/':
                a = self.s.Pop()
                b = self.s.Pop()
                self.s.Push(b/a)
            else:
                print(f"Invalid character at {self.s.array.index(x)}")
                return 3
        return self.s.Top()

expression1 = ['2','23','+','11','12','13','-','*','-']