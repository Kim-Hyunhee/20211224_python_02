class User:
    def __init__(self, name, birth_year, point) :
        self.name = name
        self.birth_year = birth_year
        self.point = point
        
    def get_age(self, year):
        age = year - self.birth_year + 1
        return age
    

        