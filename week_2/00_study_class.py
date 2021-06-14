class Person:
    def __init__(self, param_name):
        print("created",self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다.")
    pass

person_1 = Person("유재석")
print(person_1.name)
person_1.talk()
person_2 = Person("지금이순간")
print(person_2.name)