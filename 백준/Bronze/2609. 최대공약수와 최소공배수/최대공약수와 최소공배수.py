# 유클리드 호제법
# 최대공약수 -> gcd, 최대공배수 -> lcm
import sys

# 자연수 입력
numA, numB = map(int, sys.stdin.readline().split())

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 최대공약수
gcd = get_gcd(numA, numB)

# 최소공배수
lcm = numA * numB // gcd

print(gcd)
print(lcm)