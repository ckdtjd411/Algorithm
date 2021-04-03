'''
    로프 https://www.acmicpc.net/problem/2217

    [접근]
    중량에 따른 로프를 정렬한다. 최대 중량을 들어올릴 수 있는 로프부터 시작해서 순차적으로 내려온다.
    이전의 로프가 있다면 그 이후의 로프는 그 중량을 들어올릴 수 있다.
'''
line = int(input())

weight = []
for i in range(line):
    weight.append(int(input()))

weight.sort()

result = 0

for i in range(line):
    if result < weight[-1-i]*(i+1):
        result = weight[-1-i]*(i+1)

print(result)
