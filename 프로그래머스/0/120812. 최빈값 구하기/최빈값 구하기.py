import collections
def solution(array):
    counts = collections.Counter(array).most_common()  
    if len(counts) > 1 and counts[0][1] == counts[1][1]:
        return -1
    return counts[0][0]
