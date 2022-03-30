# 최대 공약수

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# gcd(60, 24) = gcd(24, 60 % 24) = gcd(24, 12) = gcd(12, 24 % 12) = ged(12, 0)

print(gcd(1, 5))
print(gcd(12, 6))
print(gcd(60, 24))

