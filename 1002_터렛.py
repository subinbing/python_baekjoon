# 조규현의 좌표: (x1, y1) / 조규현이 계산한 류재명과의 거리: r1
# 백승환의 좌표: (x2, y2) / 백승환이 계산한 류재명과의 거리: r2
# 입력 >> 첫쨰줄: 테스트 케이스의 개수 T / 둘째줄: 한 줄에 공백으로 구분된 여섯 정수 x1, y1, r1, x2, y2, r2
# 최종 출력: 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램
#          각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수 출력
#          만약, 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1 출력


import math

def distance(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if d == 0 and r1 == r2:
        return -1

    elif d == r1 + r2:
        return 1

    elif d == abs(r1 - r2):
        return 1

    elif abs(r1 - r2) < d < r1 + r2:
        return 2

    else:
        return 0

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    result = distance(x1, y1, r1, x2, y2, r2)
    print(result)
