'''
    ATM

    N명의 사람들이 돈을 인출하는데 각각 시간이 다르다.
    필요한 시간의 합의 최솟값을 구하라

    [접근]
    빨리 걸리는 사람이 먼저 줄을 서서 돈을 인출한다.
    자신이 기다린 시간 + 자신의 인출 시간 을 누적
'''

N = int(input())
time = list(map(int, input().split()))

time.sort()
total = 0

for i, j in enumerate(time):
    waiting = sum(time[:i])
    total += (waiting + j)

print(total)
