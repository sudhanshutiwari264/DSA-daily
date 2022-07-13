def sumOrProduct(n, q):

    # Write your Code here.
    if q == 1:
        return int((n/2)*(2 + (n-1) * 1))
    elif q == 2:
        pro = 1;
        for x in range(1,n+1):
            pro*=x
        return pro%((10**9) + 7 )
