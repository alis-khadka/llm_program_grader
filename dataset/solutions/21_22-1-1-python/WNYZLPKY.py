def calc(n):
    def two_in_degree(k):
        if k == 0:
            return 1
        else:
            if k % 2 == 0:
                two_in_k_dev_2 = two_in_degree(k // 2)
                exp = two_in_k_dev_2 * two_in_k_dev_2
            else:
                exp = two_in_degree(k - 1) * 2
            return exp if exp < 1000000007 else exp % 1000000007
    
    return (two_in_degree(n) - 1) % 1000000007