from card import Card

# 두장의 카드 생성.

card1 = Card('스페이드', 2)
card2 = Card('하트', 7)

# Card의 가로 길이 (Card 클래스 자체의 속성) 4로 변경
Card.width = 4
# Card의 가로/세로 길이는 클래스 변수 => Card.변수로 접근 가능
# 각 카드 객체의 무늬 / 숫자는 각 객체에 연결된 변수 => Card.변수 접근 불가능
# print(Card.pattern) 이런 행위는 불가함

# 두장의 카드 각각의 가로 길이 출력
print(f'스페이드2의 가로길이 : {card1.width}')
print(f'하트7의 가로길이 : {card2.width}')

print(f'카드 전체의 가로길이 : {Card.width}')

# 카드 클래스 자체의 기능 클래스 설명 기능 실행
Card.print_card_class_info()