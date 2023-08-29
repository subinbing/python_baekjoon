N = int(input())
count_0 = 0
count_1 = 0

for i in range(N):
    opinion = int(input())
    if opinion == 0:
        count_0 += 1
    elif opinion == 1:
        count_1 += 1

if count_0 > count_1:
    print("Junhee is not cute!")
elif count_0 < count_1:
    print("Junhee is cute!")