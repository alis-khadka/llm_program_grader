def opt(W):
    n = len(W)-1
    memo = [-1] * (n+1)
    return opt_help(n, W, memo)
    
    
def opt_help(n, W, memo):
    if n == 0:
        return W[0]
    if n == 1:
        return max(W[0], W[1])
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = max(W[n] + opt_help(n-2, W, memo), opt_help(n-1, W, memo))
        return memo[n]