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