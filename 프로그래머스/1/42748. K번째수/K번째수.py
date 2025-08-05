def solution(array, commands):
    arr = []

    for i in commands :
        arr.append(list(sorted(array[i[0]-1 : i[1]]))[i[2]-1])
    
    return arr