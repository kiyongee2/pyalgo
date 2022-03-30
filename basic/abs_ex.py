

# 절대값 1
import math


def abs_sign(x):
    if x < 0:
        return -x
    else:
        return x

# 절대값 2
def abs_square(x):
    y = x * x
    return math.sqrt(y)

print(abs_sign(4))
print(abs_sign(-5))
print('*'*10)
print(abs_square(4))
print(abs_square(-5))