round_count = int(input())

c_score = 100
s_score = 100

for i in range(1, round_count+1):
    num1, num2 = map(int, input().split())

    if(num1 > num2):
        s_score -= num1
    elif(num1 < num2):
        c_score -= num2

print(c_score)
print(s_score)