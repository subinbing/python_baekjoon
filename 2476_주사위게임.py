N = int(input())
result = 0

for i in range(N):
    num1, num2, num3 = map(int, input().split())

    if num1 == num2 == num3:
        result = max(result, 10000 + num1 * 1000)
    elif num1 == num2:
        result = max(result, 1000 + num1 * 100)
    elif num2 == num3:
        result = max(result, 1000 + num2 * 100)
    elif num1 == num3:
        result = max(result, 1000 + num1 * 100)
    else:
        big = max(num1, num2, num3) * 100
        result = max(result, big)

print(result)