# 동명이인 찾기

def find_same_name(a):
    same_name = []
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[i]==a[j]:
                same_name.append(a[i])
    return same_name

name = ['kim', 'lee', 'han', 'kim', 'han']
print(find_same_name(name))