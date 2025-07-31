# 리트코드 42번 문제 빗물 고임
barrier = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# 책에 있는 풀이
def trap(height) :
    stack = []
    volume = 0

    for i in range(len(height)) :
        while stack and height[i] > height[stack[-1]] :
            top = stack.pop()

            if not len(stack) :
                break

            distance = i - stack[-1] - 1
            water = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * water

        stack.append(i)
    return volume

# 리트코드 15번 문제 세 수의 합
# 생각해낸 방식 - 브루트 포스
nums = [-1, 0, 1, 2, -1, -4]

def three_to_zero(numbers) :
    combination = []

    for i in range(len(numbers) - 2) :
        for j in range(i+1, len(numbers) - 1) :
            for k in range(j+1, len(numbers)) :
                if numbers[i] + numbers[j] + numbers[k] == 0 :
                    combination.append([numbers[i], numbers[j], numbers[k]])

    return combination

# 책이 제시한 풀이
def combo(numbers) :
    results = []
    numbers.sort()

    for i in range(len(numbers) - 2) :
        if i > 0 and numbers[i] == numbers[i-1] :
            left, right = i+1, len(numbers)-1

            while left < right :
                sum = numbers[i] + numbers[left] + numbers[right]

                if sum < 0 :
                    left += 1
                elif sum > 0 :
                    right -= 1
                else :
                    results.append([numbers[i], numbers[left], numbers[right]])

                    while left < right and numbers[left] == numbers[left + 1] :
                        left += 1

                    while left < right and numbers[right] == numbers[right - 1] :
                        right -= 1

                    left += 1
                    right -= 1

        return results

# 리트코드 561번 문제
array = [1, 4, 3, 2]

# 내가 생각한 풀이
def min_combo(numbers) :
    numbers.sort()

    return min(numbers[0], numbers[1]) + min(numbers[2], numbers[3])

# 책이 제시한 풀이
def arraypairs(numbers) :
    sum = 0
    numbers.sort()

    for i, n in enumerate(numbers) :
        if i % 2 == 0 :
            sum += n

    return sum

def arraypairsum(nums) :
    return sum(sorted(nums)[::2])

