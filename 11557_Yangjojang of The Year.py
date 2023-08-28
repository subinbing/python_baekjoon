T = int(input())

for _ in range(T):
    N = int(input())
    max = 0
    school = ""

    for _ in range(N):
        S, L = input().split()
        L = int(L)
        if(L > max):
            max = L
            school = S
    print(school)



