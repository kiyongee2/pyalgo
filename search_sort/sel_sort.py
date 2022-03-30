# 선택 정렬
# 주어진 리스트에서 최소값을 반환하는 함수
def find_min_idx(a):
    min_idx = 0
    n = len(a)
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

# 선택 정렬 함수
def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)   # 최솟값을 꺼내서 value에 저장
        result.append(value)
    return result

v = [2, 4, 5, 1, 3]
sort_v = sel_sort(v)
print(sort_v)
