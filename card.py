# 개념 설명을 클래스
# 포커 카드를 표현하는 클래스

class Card:
    
     # 카드의 가로길이 / 세로길이 => 각각이 별개로 갖는 게 아니라 모든 카드가 공유해야 하는 값 (같은 값 유지)
     # 여기에 만든 변수들은 클래스 변수로 동작 => 모든 객체가 동일한 값을 갖는다.
     width = 5
     height = 7
    
     def __init__(self, pattern, number):
         # 객체 변수 => 각 카드 한장 한장이 갖는 모양 / 숫자
        self.pattern = pattern
        self.number = number
        
     # 이 카드 클래스 자체에 대한 설명을 출력하는 메쏘드
     @classmethod  # 이 메쏘드가 클래스 자체의 기능임을 나타냄
     def print_card_class_info(cls):  # cls : class 종류 자체가 뭔지를 알려주는 역할
          print('이 카드는 포커 카드를 표현하는 클래스 입니다.')
          print(f'우리가 만든 카드의 가로 길이는 {cls.width} 입니다.')  # 해당 클래스의 클래스 변수를 끌어다 쓰려는 상황
          print(f'세로 길이는 {cls.height} 입니다.')