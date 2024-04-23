N = int(input())
a = list(map(int, input().split()))

dict = set()
for n in a:
    dict.add(n)
print(len(dict))
