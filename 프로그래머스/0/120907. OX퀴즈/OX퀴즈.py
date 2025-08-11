def solution(quiz):
    answer = []
    
    for q in quiz :
        part = q.split()
        
        if part[1] == '+' :
            answer.append('O' if int(part[0]) + int(part[2]) == int(part[4]) else 'X')
            
        if part[1] == '-' :
            answer.append('O' if int(part[0]) - int(part[2]) == int(part[4]) else 'X')
    
    return answer
