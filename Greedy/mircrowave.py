'''
    전자레인지 https://www.acmicpc.net/problem/10162

    [접근]
    가장 오래 걸리는 시간부터 사용한다.
'''


time = int(input())

timer = [300, 60, 10]
count = [0, 0, 0]

if time % timer[-1]:
    print(-1)
else:
    for i in range(len(timer)):
        count[i] += (time // timer[i])
        time %= timer[i]

    for i in range(len(count)):
        print(count[i], end=' ')
