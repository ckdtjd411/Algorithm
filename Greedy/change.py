"""
    거스름돈 https://www.acmicpc.net/problem/5585
    최소한의 동전 개수로 거스름돈을 돌려주는 문제

    O(N) : 화폐의 종류만큼만 비교
"""

change = 1000 - int(input())
coin_types = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coin_types:
    count += change // coin
    change %= coin

print(count)
