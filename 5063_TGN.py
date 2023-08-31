N = int(input())

'''
N: 테스트 케이스의 개수
r: 광고를 하지 않았을 때 수익
e: 광고를 했을 때의 수익
c: 광고 비용 
'''
def cal():
    if r < e - c:
        print("advertise")
    elif r == e - c:
        print("does not matter")
    else:
        print("do not advertise")

for _ in range(N):
    r, e, c = map(int, input().split())
    cal()
