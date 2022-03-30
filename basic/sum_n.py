# 1+2+3+...+n
# 알고리즘1
def sum_n(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    return sum_v

print(sum_n(10))
print(sum_n(100000000))


