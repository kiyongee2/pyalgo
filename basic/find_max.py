# 최대값
def find_max(a):
    max_v = a[0]
    n = len(a)
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

v = [10, 20, 89, 100, 60, 50 , 90]
print(find_max(v))