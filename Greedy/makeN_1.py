'''
    어떠한 수 N이 1이 될때까지 두 과정 중 하나를 반복하적으로 선택하여 수행한다.
        1. N에서 1을 뺀다.
        2. N을 K로 나눈다.
    N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수

    O(log n) : N의 크기를 반으로 줄여나감. 
'''

n, k = map(int, input().split())
count = 0

while True:
    target = (n // k) * k   # N에서 1을 빼야하는 횟수
    count += (n - target)
    n = target
    if n < k:
        break
    count += 1
    n //= k

count += (n - 1)
print(count)