# 과자 가격 K, 사려고 하는 과자 개수 N, 동수가 가진 돈 M
K, N, M = map(int, input().split())

if K * N > M:
    result = K * N - M
    print(result)
elif K * N < M or K * N == M:
    print(0)