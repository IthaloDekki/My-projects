# FIBONACCI
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# FATORIAL
def fatorial(n):
    if n <=1:
        return 1
    else:
        return n * fatorial(n-1)
    
# DEIVIS
def deivis(n):
    if n <=1:
        return 1
    elif n == 2:
        return 2
    else:
        return((deivis(n-1)) + (deivis(n-2))-1)