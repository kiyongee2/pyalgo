# 이분 탐색
def binary_search(a, x):
    # 탐색할 범위를 저장하는 함수
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2   #탐색 범위의 중간 위치
        if x == a[mid]:
            return mid
        elif x > a[mid]:    # 찾는값이 더 크면 오른쪽으로 범위를 좁혀 계속 탐색
            start = mid + 1
        else:
            end = mid - 1

    return -1      # 찾지 못했을때

v = [1, 4, 16, 25, 36, 49, 64, 81]
print(binary_search(v, 25))
print(binary_search(v, 64))
print(binary_search(v, 50))