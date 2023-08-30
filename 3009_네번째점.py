num_x = []
num_y = []

for i in range(3):
    x, y = map(int, input().split())
    num_x.append(x)
    num_y.append(y)

for i in range(3):
    # 세 점 중에서 한 번만 언급된 것을 찾기
    if num_x.count(num_x[i]) == 1:
        x4 = num_x[i]
    if num_y.count(num_y[i]) == 1:
        y4 = num_y[i]
print(x4, y4)



