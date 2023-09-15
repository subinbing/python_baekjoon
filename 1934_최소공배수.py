T = int(input())

# 최소공배수 => a, b의 곱을 a, b의 최대공약수로 나누면 나옴
# 최대공약수 => A/B -> B=A%B => B가 0이될 때까지 반복 => 최대공약수: 남는 A값
for i in range(T):
    A, B = map(int, input().split())
    m = A * B

    # 최대공약수
    while B > 0:
        A, B = B, A % B

    # 최소공배수
    print(m // A)