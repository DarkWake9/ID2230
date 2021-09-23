class Stacks:
    def __init__(self, stack):
        self.stack = stack
    
    def createemptystack(stack):
        stack = []
        return stack

    def Push(stack, x):
        stack = stack.append(x)
        print(f"{x} is appended to the stack")
        return 0

    def Pop(stack):
        k = stack.pop(len(stack)-1)
        return k

    def Top(stack):
        return stack[len(stack)-1]

    def IsEmpty(stack):
        if len(stack) == 0:
            print("Stack is Empty")
            return 0
        else:
            print("Stack is Not Empty")
            return 1


##Driver code
stack = Stacks()
print(stack)