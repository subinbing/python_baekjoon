# A: 저작권이 있는 멜로디의 총 개수
# B: 앨범에 수록된 곡의 개수
# I: 평균값
A, I = map(int, input().split())
B = A * (I - 1) + 1
print(B)
