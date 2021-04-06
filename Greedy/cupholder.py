'''
    컵홀더 https://www.acmicpc.net/problem/2810

    [접근]
    컵홀더 수는 N+1
    한 커플마다 사용할 수 있는 컵홀더 수가 1개씩 줄어든다
'''

import sys

holders = int(input()) + 1
batch = sys.stdin.readline()

couple = int(batch.count('LL'))

if couple <= 1:
    print(num)
else:
    print(holders - couple + 1)
