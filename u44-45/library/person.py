class Person:    # 클래스 #45에서 긁어옴/살짝 고치기 
    def __init__(self, name, age, address='부산 연제구'):
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다.')