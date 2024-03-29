def solution(participant, completion):
    '''
    input
        - participant : [참가자] (1 < 100,000)
        - completion  : [완주자] (len(participant) - 1)
    output
        - answer      : 완주하지 못한 사람
    result
        - 정확성 : 100/100
        - 효율성 : 100/100
    '''
    result = dict()

    for name in participant:
        if name not in result:
            result[name] = 0
        result[name] += 1

    for name in completion:
        result[name] -= 1

    for name in participant:
        if result[name] == 1:
            return name

print(solution(
    ['leo', 'kiki', 'eden'],
    ['eden', 'kiki']
)) # => 'leo'

print(solution(
    ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
    ['josipa', 'filipa', 'marina', 'nikola']
)) # => 'vinko'

print(solution(
    ['mislav', 'stanko', 'mislav', 'ana'],
    ['stanko', 'ana', 'mislav']
)) # => 'mislav'
