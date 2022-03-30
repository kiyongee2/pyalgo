# 동명이인 찾기
# 입력 - 이름이 n개 들어있는 리스트
# 출력 - n개의 이름 중 반복되는 이름의 집합

def find_same_name(a):
    name_dict = {}

    for name in a:
        if name in name_dict:
            name_dict[name] += 1 # 등장횟수를 1증가
        else:
            name_dict[name] = 1  # 등장횟수를 1로 저장

    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name = ["콩쥐", "팥쥐", "흥부", "놀부", "콩쥐"]
print(find_same_name(name))
