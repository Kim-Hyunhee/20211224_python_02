class Book:
    def __init__(self, title, rent_fee, limit_age):
        self.title = title
        self.rent_fee = rent_fee
        self.limit_age = limit_age
        self.rent_user = None
        
    def print_book_info(self):
        print('===== 책 정보 출력 =====')
        print(f'책 이름 : {self.title}')
        print(f'대여료 : {self.rent_fee} P')
        print(f'연령 제한 : {self.limit_age} 세')
        
        if self.rent_user :
            pass
        else:
            print('대여해 간 사람이 없습니다.')