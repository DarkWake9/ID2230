#include <iostream>

const int maxsize = 500;
class Stacks
{
    public:
    double stack[maxsize];
    int n = -1;
    bool Push(int x, double stack[])
    {
        if (n >= (maxsize - 1))
        {
            cout << "Stack Overflow";
            return false;
        }
        else
        {
            stack[++n] = x;
        }
        return true;
    }
    bool isEmpty(double stack)
    {
        if (n == 0)
        {
            cout << "Stack is Empty"
            return true;
        }
        else return false;
    }
};