# 2025-08-07 16:20 자력 해결 실패
최대공약수 함수인 gcd의 존재를 몰랐고 수학적 논리 설계도 실패

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

0단계라는 말이 무색하게 무참하게 패배한 문제.

tip1) 자주 쓰이는 함수인 reduce, gcd, combinations 같은 메서드를 착실히 외우자
tip2) 어떤 계산 작용을 해야 하는데 그게 뭔지 안 떠오르면 함수 설계를 직접 해보자
tip3) in iterator 이 꼴은 정말 재앙이다. 눈에 들어올 때까지 사고 연습을 하자
