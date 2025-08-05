def solution(lottos, win_nums):
    answer = [0, 0]
    
    lottos.sort()
    win_nums.sort()
    
    for i in range(6) :        
        if lottos[i] == 0 or lottos[i] in win_nums :
            answer[0] += 1
        
        if lottos[i] in win_nums :
            answer[1] += 1
    
    answer[0] = min(7 - answer[0], 6)
    answer[1] = min(7 - answer[1], 6)
        
    
    return answer