# 최대값의 위치
def find_max_idx(a):
    max_idx = 0
    n = len(a)
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

v = [10, 20, 89, 100, 60, 50 , 90]
print("최대값의 위치 :", find_max_idx(v))