'''
    세탁소 사장 동혁 https://www.acmicpc.net/problem/2720

    [접근]
    큰 단위 화폐부터 거슬러 준다.
'''

count = int(input())
change = []
for i in range(count):
    change.append(int(input()))

coin_types = [25, 10, 5, 1]
coin_count = [0 for i in range(len(coin_types))]

for i in range(count):
    for j in range(len(coin_types)):
        coin_count[j] = change[i] // coin_types[j]
        change[i] = change[i] % coin_types[j]
    print('{0} {1} {2} {3}'.format(coin_count[0],coin_count[1],coin_count[2],coin_count[3]))


    
    
