# 하노이의 탑 옮기기

def hanoi(n, from_pos, to_pos, aux_pos):
    if n==1: #원반 1개를 옮기는 문제면 그냥 옮기면 됨
        print(from_pos, '->', to_pos)
        return

    # 원반 n-1개를 aux_pos로 이동(to_pos를 보조기둥으로)
    hanoi(n-1, from_pos, aux_pos, to_pos)
    # 가장 큰 원반을 목적지로 이동
    print(from_pos, '->', to_pos)
    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조기둥으로)
    hanoi(n-1, aux_pos, to_pos, from_pos)

print('n==1')
hanoi(1, 1, 3, 2) #1번
print('n==2')
hanoi(2, 1, 3, 2) #3번
print('n==3')
hanoi(3, 1, 3, 2) #7번
print('n==4')
hanoi(4, 1, 3, 2) #15번