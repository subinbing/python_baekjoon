# 테스트 케이스
T = int(input())

Y = 0
K = 0

for i in range(T):
    for j in range(0, 9):
        Y_score, K_socre = map(int, input().split())
        Y += Y_score
        K += K_socre

    if Y > K:    # 연세대가 이겼을 경우
        print('Yonsei')
    elif Y < K:    # 고려대가 이겼을 경우
        print('Korea')
    else:    # 비겼을 경우
        print("Draw")