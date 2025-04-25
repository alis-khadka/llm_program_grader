def calc(n):
    return (recursive_function(n)-1) % 1000000007




def recursive_function(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        output = recursive_function(n/2)
        return output * output % 1000000007
    else:
        return (2 * recursive_function(n-1)) % 1000000007