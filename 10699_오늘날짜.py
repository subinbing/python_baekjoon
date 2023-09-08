from datetime import datetime

# 이렇게 하면 날짜, 시간도 다 출력되기 때문
# print(datetime.now())      # 출력 예시 : 2023-09-08 09:33:41.281645

# 날짜만 출력하기 위해서는 datetim.now()를 문자열로 바꿔주고 날짜 인덱스가 0부터 9까지이므로 아래와 같음
print(str(datetime.now())[:10])    # 출력 : 2023-09-08