# # 현재시각 -> 시(A), 분(B), 초(C)
# # 요리하는 데 필요한 시간 -> D(초)
#
# A, B, C = map(int, input().split())
# D = int(input())
#
# seconds = (C + D) % 60                    # 현재 시각인 초(C)에 요리하는 데 필요한 시간 D초를 계산 => 초
#
# minutes = (C + D) // 60                   # 현재 시각인 분(B)을 포함하지 않은 분
# final_minutes = (B + minutes) % 60        # 현재 시각인 분(B)를 포함한 최종 분
#
# hours = (B + minutes) // 60               # 현재 시각인 분(B)과 minutes를 합해 그 값이 60으로 나누어 떨어진 수가 hours
# final_hours = (A + hours) % 24            # 최종 시간인 시(hour) 계산
#
# print(final_hours, final_minutes, seconds)


# 현재시각 -> 시(A), 분(B), 초(C)
# 요리하는 데 필요한 시간 -> D(초)

A, B, C = map(int, input().split())
D = int(input())

seconds = (C + D) % 60

minutes = (C + D) // 60
final_minutes = (B + minutes) % 60

hours = (A + ((B + minutes) // 60)) % 24

print(hours, final_minutes, seconds)