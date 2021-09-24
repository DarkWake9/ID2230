maxsize = 500

class Stacks:
    def __init__(self):
        self.stack = []

    def Push(self,x):
        if (len(self.stack) < maxsize):
            self.stack.append(x)
            return 0
        else:
            print("Stack Overflow")
            return 2

    def Pop(self):
        k = self.stack.pop(len(self.stack)-1)
        return k

    def Top(self):
        return self.stack[len(self.stack)-1]

    def IsEmpty(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
            return 1
        else:
            print("Stack is Not Empty")
            return 0


##Driver code
stack = Stacks()
stack.Push(10)
stack.Push(20)
stack.Push(0)
print(stack.stack)