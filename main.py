from book import Book
from user import User

book1 = Book('먼나라 이웃나라', 1500, 12)

user1 = User('김성인', 1990, 20000)

user1.print_user_info()

book1.print_book_info()

# book1을 김성인 에게 빌려줘보자

if book1.rent_book_to_user(user1):
    print(f'[{book1.title}] 도서를 {user1.name}에게 대여했습니다.')
else:
    print(f'[{book1.title}] 도서를 {user1.name}에게 대여하지 못했습니다.')    
    
    
book2 = Book('고가의 책', 20000, 15)

print( book2.rent_book_to_user(user1) )

user1.print_user_info()


book3 = Book('성인 도서', 1000, 19)

user2 = User('미성년자', 2010, 50000)

book3.rent_book_to_user(user2)