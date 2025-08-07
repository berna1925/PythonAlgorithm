def solution(a, b):  
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    b //= gcd(a, b)
    
    for p in [2, 5] :
        while b % p == 0 :
            b /= p
    
    return 1 if b == 1 else 2
