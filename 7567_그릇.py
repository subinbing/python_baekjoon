dish = input()
length = 10    # 처음 그릇 길이

for i in range(1, len(dish)):
    if dish[i] == dish[i-1]:      # 이 전의 그릇과 같은 방향이면 5cm 추가
        length += 5
    elif dish[i] != dish[i-1]:    # 이 전의 그릇과 다른 방향이면 10cm 추가
        length += 10

print(length)