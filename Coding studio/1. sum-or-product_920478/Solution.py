# My solution !
def sumOrProduct(n, q):

    # Write your Code here.
    if q == 1:
        return int((n/2)*(2 + (n-1) * 1))
    elif q == 2:
        pro = 1;
        for x in range(1,n+1):
            pro*=x
        return pro%((10**9) + 7 )

# original solution 
'''
    Time Complexity : O(N)
    Space Complexity : O(1)

    Where 'N' is the number given.
'''


def sumOrProduct(n, q):

    answer = 0
    mod = int(1e9) + 7

    if q == 1:

        # Sum of first 'N' numbers is given by
        # 'N' * 'N + 1' / 2.
        answer = (n * (n + 1)) // 2

    else:
        answer = 1
        for i in range(1, n + 1):
            # Modular Arithmatic.
            i %= mod
            answer %= mod
            answer = (((answer * i) % mod) + mod) % mod

    return answer
