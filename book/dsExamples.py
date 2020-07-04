def fibonacci( ):
    a, b = 0, 1
    while True:
        yield a
        # simultaneous assignments.Within each pass of the loop, the goal was to reassign a and b, respectively, to the values of b and a+b
        a, b = b, a+b