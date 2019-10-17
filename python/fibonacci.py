# Fibonacci sequence : F0=0,F1=1, Fn= Fn-1 + Fn-2

# recursion version, the worst

def fibo1(n: int) -> int:
    """
    simple solution looking the mathematic sequence
    """
    if n==0 :
        return 0
    if n==1 :
        return 1
    else :
        return fibo1(n-1)+fibo1(n-2) #some fibo1(i) are calculated many times

# better one, O(n)

def fibo2(n: int) -> int :
    """Evaluate the fibonacci sequence
    i and j are indicators where i corresponding to Fi
    :param n: upper bound
    :return: the `n`th element
    """
    i, j = 0, 1
    for k in range(n) :
        i, j = j, i + j
    return i