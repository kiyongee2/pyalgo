# 자신의 모든 친구를 찾는 알고리즘
# 입력 : 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력 : 모든 친구의 이름

def print_all_friends(g, start):
    qu = []       # 앞으로 처리해야할 사람들 저장
    done = set()  # 이미 큐에 추가한 사람들을 집합에 기록(중복 방지)

    qu.append(start)  # 자신을 큐에 넣고 시작
    done.add(start)   # 집합에도 추가

    while qu:         # 큐에 처리할 사람이 남아 있는 동안
        p = qu.pop(0) # 큐에서 처리 대상을 한명 꺼내
        print(p)
        for x in g[p]: # 친구가 있는 동안
            if x not in done:  # 아직 큐에 추가된적이 없는 사람을
                qu.append(x)
                done.add(x)

# 친구 관계 리스트
# A와 B가 친구이면
# A의 친구 리스트에도 B가 나오고, B의 친구리스트에도 A가 나옴

fr_info = {
    'Summer': ['John', 'Justine', 'Mike'],
    'John': ['Summer', 'Justine'],
    'Justine': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justine'],
    'May': ['Justine', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(fr_info, 'Summer')
print('*' * 10)
print_all_friends(fr_info, 'Jerry')