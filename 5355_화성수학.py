# 테스트 케이스의 개수 입력
T = int(input())

# 테스트 케이스의 개수만큼 반복
for i in range(T):
    num = list(map(str, input().split()))        # 입력 받아서 split
    num_first = eval(num[0])                     # num의 첫 번째 문자열 저장

    for j in range(len(num)):
        if num[j] == '@':
            num_first = num_first * 3
        elif num[j] == '%':
            num_first = num_first + 5
        elif num[j] == '#':
            num_first = num_first - 7

    print("%0.2f" % num_first)
