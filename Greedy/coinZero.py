'''
    동전 0 https://www.acmicpc.net/problem/11047
    입력: N, K    N: 동전 단위 수, K: 합
         Ai      A: 동전 단위 (오름차순)

    [접근]
    큰 단위의 동전부터 선택해 다음 단위 동전에 대해 반복하여 수행한다.
'''

typeN, total = map(int, input().split())

coin_list = []
for i in range(typeN):
    coin_list.append(int(input()))

coin_list.reverse()
count = 0

for i in range(typeN):
    count += total // coin_list[i]
    total %= coin_list[i]

print(count)