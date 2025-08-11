# 2025-08-11 15:35 자력 해결
def solution(arr, query):
    
    for i in range(len(query)) :
        if i % 2 == 0 :
            arr = arr[:query[i]+1]
        
        if i % 2 == 1 :
            arr = arr[query[i]:]   
    
    return arr

* 매번 슬라이싱을 하는 상당히 억척스러운 구조
* 딱 봐도 파이썬스러운 자연스러움이 부족함

============ 대안적 풀이 ==============
@ enumerate 활용
def solution(arr, query):
    start, end = 0, len(arr) - 1
    
    for i, q in enumerate(query):
        if i % 2 == 0:  
            end = start + q
        else:          
            start = start + q
    
    return arr[start:end+1]

- 인덱스를 활용하는 문제에선 enumerate를 잘 쓰면 좋은 점이 많다
- 초기 값을 할당하고 그 값을 어떻게 누산해 갈 것인지 설계하는 것도 알고리즘의 미덕 중 하나

