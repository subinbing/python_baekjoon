# S: 서로 다른 N개의 자연수 합

S = int(input())
N = 0
res = 0

for i in range(1, S+1):    # S까지 1을 차례대로 더함
    res += i
    N += 1
    if(res > S):        # 그 값이 S보다 커지면 N-1이 N의 최댓값
        N -= 1
        break

print(N)