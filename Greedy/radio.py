'''
    라디오 https://www.acmicpc.net/problem/3135

    [접근]
    입력받은 리스트 내에 b와 비교해 가장 작은 값을 도출
    a와 b의 차이의 절댓값과 가장 작은 값 + 1 을 비교
'''

a, b = map(int, input().split())
n = int(input())

nlist = []
for i in range(n):
    nlist.append(int(input()))

dif = min(list(map(abs, [nlist[i] - b for i in range(n)])))

if abs(a - b) < (dif + 1):
    print(abs(a - b))
else:
    print(dif + 1)
