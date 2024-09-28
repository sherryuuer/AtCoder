# https://atcoder.jp/contests/past201912-open/tasks/past201912_b
N = int(input())
A = [int(input()) for _ in range(N)]

for i in range(1, N):
    if A[i] > A[i - 1]:
        print(f'up {A[i] - A[i - 1]}')
    elif A[i] < A[i - 1]:
        print(f'down {A[i - 1] - A[i]}')
    else:
        print('stay')
