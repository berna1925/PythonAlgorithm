def solution(arr, query):
    
    for i in range(len(query)) :
        if i % 2 == 0 :
            arr = arr[:query[i]+1]
        
        if i % 2 == 1 :
            arr = arr[query[i]:]   
    
    return arr