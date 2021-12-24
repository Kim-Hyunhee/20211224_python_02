# (my_math) 모듈 내부의 함수 (add)를 따로 불러와 바로 사용
# my_math.add 로 활용하기 번거롭다.

from my_math import *   # 해당 모듈의 모든 함수 불러내기

mul(10, 20)

add(10, 20)

div(10, 20)