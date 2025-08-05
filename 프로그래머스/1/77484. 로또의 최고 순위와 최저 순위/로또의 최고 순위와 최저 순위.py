# 2025-08-05 자력 풀이(파이썬 튜터 참조)
def solution(lottos, win_nums):
    answer = [0, 0]
    
    for i in range(6) :        
        if lottos[i] == 0 or lottos[i] in win_nums :
            answer[0] += 1
        
        if lottos[i] in win_nums :
            answer[1] += 1
    
    answer[0] = min(7 - answer[0], 6)
    answer[1] = min(7 - answer[1], 6)
        
    return answer

elif는 if 조건이 False가 나왔을 때만 작동하는 가정문이기 때문에
사용할 수 있는 조건이 더욱 한정적이다..

참고로 챗GPT는 아래와 같은 코드를 작성했다.
순서 상관없이 판단하려고 in을 쓴 건데 AI는 set 자료형을 사용했다.
의외로 쓸 만한 구석이 많으니 set의 &, - 연산자는 적극 활용하도록 하자.

def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    correct = len(set(lottos) & set(win_nums))
    
    max_rank = min(7 - (correct + zero_count), 6)
    min_rank = min(7 - correct, 6)
    
    return [max_rank, min_rank]
