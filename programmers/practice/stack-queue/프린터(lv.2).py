def solution(priorities, location):
    '''
    input
        - priorities : [인쇄 중요도] (1 <= [] <= 100, 1 <= i <= 9)
        - location : 요청한 문서의 인덱스 (0 <= i <= len(priorities) - 1)
    output
        - answer : 요청된 문서가 출력되는 순서
    '''
    from collections import deque

    task_queue = deque(map(
        lambda _: (priorities[_], _ == location),
        range(len(priorities))))
    task_stack = sorted(priorities)
    urgent     = task_stack.pop()
    answer     = 0

    while True:
        priority, is_target = task_queue.popleft()

        if priority == urgent:
            answer += 1

            if is_target:
                return answer

            urgent = task_stack.pop()

            continue

        task_queue.append((priority, is_target))

print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
