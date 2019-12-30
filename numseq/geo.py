def square(n):
    return n**2


def triangle(n):
    if n < 0:
        return 0
    else:
        return n + triangle(n-1)

def cube(n):
    return n**3
