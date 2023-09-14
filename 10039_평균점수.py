sc = 0

for i in range(5):
    score = int(input())

    if score < 40:
        sc += 40
    else:
        sc += score

result = round(sc / 5)
print(result)