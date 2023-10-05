T = int(input())

A = 0    # A : 300초
B = 0    # B : 60초
C = 0    # C : 10초

if T % 10 != 0:    # 10초로 나눠 떨어지지 않으면
    print(-1)      # -1 출력

else:
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10

    print(A, B, C)