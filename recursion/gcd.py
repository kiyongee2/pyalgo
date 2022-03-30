# 최대 공약수
# 4, 6의 최대공약수

def gcd(a, b):
    i = min(a, b)  #최소값을 i에 저장
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

print(gcd(1, 5))
print(gcd(4, 6))

