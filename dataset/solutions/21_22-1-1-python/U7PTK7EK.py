MOD_NUMBER = 1000000007

def exp_2(n):
    n_binary = format(int(n), "b")[::-1]
    y = 1
    z = 2
    
    for i in range(0, len(n_binary)):

        if n_binary[i] == "1":
            y = (y * z) % MOD_NUMBER
        z = z * z % MOD_NUMBER

    return y
    
def calc(n_0):
    return (exp_2(n_0) - 1) % MOD_NUMBER