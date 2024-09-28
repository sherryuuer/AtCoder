def double_or_error(S):
    # 入力が3桁の数字で構成されているかどうかを確認
    if S.isdigit() and len(S) == 3:
        # 3桁の整数ならその2倍を計算して出力
        print(int(S) * 2)
    else:
        # それ以外の場合は "error" を出力
        print("error")


# 入力を受け取る，我是没想到，不通过的原因是不能在input里写提示
S = input()
double_or_error(S)

# https://atcoder.jp/contests/past201912-open/tasks/past201912_a

# S = input()

# for i in range(3):
#     if S[i] not in '0123456789':
#         print('error')
#         exit()
# print(int(S) * 2)
