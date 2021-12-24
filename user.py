class User:
    def __init__(self, name, birth_year, point) :
        self.name = name
        self.birth_year = birth_year
        self.point = point
        
    def get_age(self, year):
        age = year - self.birth_year + 1
        return age
    
    def print_user_info(self):
        print("===== 사용자 정보 출력 =====")
        print(f'이름 : {self.name}')
        print(f'나이 : {self.get_age(2021)} 세')
        print(f'보유 포인트 : {self.point} P')
        