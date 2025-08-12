# def solution(board):
#     answer = 0
    
#     for i in range(len(board)):
#         for j in range(len(board)) :
#             if board[i][j] == 1 :
#                 board[i][min(0, i-1) : min(0, i-1)+3] = 1
                
    
#     return answer


def solution(board):
    n = len(board)
    danger = set()
    
    # 8방향 + 자기 자신
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),  (0,0),  (0,1),
                  (1,-1),  (1,0),  (1,1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: 
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        danger.add((ni, nj))
    
    # 안전지역 = 전체 칸 수 - 위험지역 수
    return n * n - len(danger)
