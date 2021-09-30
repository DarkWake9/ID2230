maxsize = 500

class Stacks:
    def __init__(self):
        self.array = []

    def Push(self,x):
        if (len(self.array) < maxsize):
            self.array.append(x)
            return 0
        else:
            print("Stack Overflow")
            return 2

    def Top(self):
        return self.array[len(self.array)-1]

    def IsEmpty(self):
        if len(self.array) == 0:
            print("**Stack is Empty**")
            return 1
        else:
            return 0
    
    def Pop(self):
        if self.IsEmpty() == 0:
            popped = self.array.pop(len(self.array)-1)
            return popped
        else:
            print("Stack Empty")
            return 1