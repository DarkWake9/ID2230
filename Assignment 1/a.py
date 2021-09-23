Maxsize = 500

def createemptystack(): #Creates Empty Stack
    stack = []
    return stack


def Push(stack, x): #To Push a new element onto the stack
    if (len(stack) < Maxsize):
        stack = stack.append(x)
        return 0
    else:
        print("Stack Overflow")
        return 2

def Pop(stack): #Removes the latest added element from the stack and returns it
    k = stack.pop(len(stack)-1)
    return k

def Top(stack): #Returns the last element added to the stack
    return stack[len(stack)-1]

def IsEmpty(stack): #Checks whether the stack is empty
    if len(stack) == 0:
        print("Stack is Empty")
        return 0
    else:
        print("Stack is Not Empty")
        return 1


##Driver code
st = createemptystack()
print(st)
Push(st, 10)
print(st)
Push(st, 20)
print(st)
Push(st, 30)
print(st)
print(f"{Pop(st)} has been removed")
print(st)
Push(st, 2  )
print(st)
print(Top(st))