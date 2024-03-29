def solution(prices):
    '''
    input
        - prices : [주식가격] (2 <= [] <= 100000, 1 <= i <= 10000)
    output
        - answer : 각 시점마다 주식이 떨어지지 않은 기간
    result
        - 정확성 : 100/100
        - 효율성 : 100/100
    '''
    answer = []
    maximum = len(prices) - 1

    for current in range(maximum):
        price = prices[current]
        time  = 0
        while current + time < maximum:
            time += 1
            if price > prices[current + time]:
                break
        answer.append(time)
    answer.append(0)

    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
