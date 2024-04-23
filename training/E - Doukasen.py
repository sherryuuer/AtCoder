N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
# lst = [[1, 1], [2, 1], [3, 1]]
time = 0
for i, j in lst:
    time += i / j

half_time = time / 2
length = 0
for i, j in lst:
    if i / j <= half_time:
        length += i
        half_time -= i / j
    elif i / j > half_time:
        length += half_time * j
        break
print("{:.15f}".format(length))
# 这里的小数点处理是关键，关系到精度和正确与否


# 或者这么写很好
t = sum(ai / bi for ai, bi in zip(a, b)) / 2
ans = 0
for ai, bi in zip(a, b):
    ans += min(ai, t * bi)
    t -= min(ai / bi, t)

print("{:.15f}".format(ans))
