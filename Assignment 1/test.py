from oop1 import Stacks
##Driver code
stack = Stacks()
stack.Push(10)
stack.Push(20)
print(stack.array)
#stack.Push(0)
print(f"{stack.Top()}")
stack.Pop()
print(stack.array)
stack.Pop()
print(stack.array)
stack.Pop()
print(stack.array)