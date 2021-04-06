'''
    설탕 배달 https://www.acmicpc.net/problem/2839

    N킬로그램을 배달해야하는데 3킬로그램, 5킬로그램 봉지를 이용한다.
    최소 봉지 개수를 구하라. 정확히 N킬로그램을 만들 수 없다면 -1 출력

    [접근]
    5kg로 담을 수 없으면 3kg로 담아야 한다.
    먼저 5kg 봉지로 담을 수 있으면 담고 3kg로 하나씩 담는다.
'''

sugar = int(input())
bag = 0

while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1

    if sugar < 0:
        print(-1)



