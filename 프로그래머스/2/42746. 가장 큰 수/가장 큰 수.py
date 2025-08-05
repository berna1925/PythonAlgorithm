def solution(numbers):
    리스트 속 숫자를 문자열로 바꾸려면 map 함수를 반드시 써야 한다!
    str() 이런 것은 통하지 않는다
    numbers = list(map(str, numbers))
    
    numbers.sort(key=lambda x : x * 3, reverse=True)

    입력이 전부 0이었을 때는 0000이 아니라 0이 반환되도록 예외 처리
    if numbers[0] == '0':
        return '0'

    이어 붙일 도구 + join(붙일 대상)이다...
    return ''.join(numbers)
    
