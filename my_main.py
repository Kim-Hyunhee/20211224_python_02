# (my_math) 모듈 내부의 함수 (add)를 따로 불러와 바로 사용
# my_math.add 로 활용하기 번거롭다.

from my_math import add, mul, div   # 하나의 모듈에서 여러 개의 함수를 한꺼번에 불러올 수 있다.

mul(10, 20)

add(10, 20)

div(10, 20)