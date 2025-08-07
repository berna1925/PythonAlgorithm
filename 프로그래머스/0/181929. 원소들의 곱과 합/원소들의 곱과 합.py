# 2025-08-07 15:10 풀이
0단계는 정답률 50%까지 패스하기로...
    
def solution(num_list):
    mul = 1
    sum = 0
    
    for num in num_list :
        mul *= num
        sum += num
        
    if mul < sum ** 2 :
        return 1
    elif mul > sum ** 2:
        return 0


**better way to solve**

def solution(num_list):
    from functools import reduce
        return int(reduce(lambda x, y: x * y, num_list) < sum(num_list) ** 2)

tip1) map과 유사한 functools.reduce & lambda의 기능을 활용하면 함수적 연산을 쉽게 적용 가능
tip2) 숫자 (등호/부등호) 숫자 의 결과는 True, False 둘 중 하나이므로 그것을 int로 환산해 결론 내는 방식
