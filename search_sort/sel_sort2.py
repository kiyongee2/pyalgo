# 선택정렬2

def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i] # 교환

v = [7, 9, 1, 5, 8]
sel_sort(v)
print(v)