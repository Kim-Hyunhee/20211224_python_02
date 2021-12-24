# 개념 설명을 클래스
# 포커 카드를 표현하는 클래스

class Card:
    
      def __init__(self, pattern, number):
        # 객체 변수 => 각 카드 한장 한장이 갖는 모양 / 숫자
        self.pattern = pattern
        self.number = number