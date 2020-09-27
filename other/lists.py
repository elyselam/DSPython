def fib(n):
    a = 0
    b = 1
    if n <= 0:
        print("incorrect input")
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a+b
            a = b
            b = c
        return b





def fibRec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibRec(n-1)+fibRec(n-2)