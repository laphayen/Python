
# 모듈
# 독립된 코드
# import 모듈이름
# import 패키지이름.모듈이름

# 다른 파일 저장 후 import로 모듈 사용 가능 - 저장한 이름.py와 이름이 동일

# import
import time
print("10초 정지")
time.sleep(10)
print("10초 후 출력")

# 계층 구조는 from 파일 사용
from time import sleep
sleep(10)
print("print")

 # 이름이 길 경우 as 별칭으로 사용
 import 모듈이름 as 별칭
 