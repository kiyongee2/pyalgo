# 1부터 n까지의 곱
# 1 x 2 x 3.... x n
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(1))
print(facto(4))