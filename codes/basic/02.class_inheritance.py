# class class_name(): 
#     변수
#     def __init__(self):
#         pass

'''
1. 상속이란?
상속은 기존 클래스(부모 클래스)의 속성과 메서드를 새로운 클래스(자식 클래스)가 물려받는 것을 의미합니다.

부모 클래스의 기능을 자식 클래스가 그대로 사용할 수 있습니다.
자식 클래스는 필요에 따라 부모 클래스의 기능을 확장하거나 **재정의(override)**할 수 있습니다.
'''

# (1) 부모 클래스: Animal
class Animal():
    def __init__(self, name = 'JuJu'):
        self.name = name
        pass
    
    def speak(self, species):
        # return f'{self.name}는 {species} 종입니다.'
        return f'{species} 종입니다.'

    # Animal은 부모 클래스입니다.
    # 이 클래스는 모든 동물에 공통적인 특징(예: 이름, 말하는 행동)을 정의합니다.

# (2) 자식 클래스: Dog와 Cat
    # Dog와 Cat은 각각 부모 클래스인 Animal을 상속받았습니다.

class Dog(Animal):
    def __init__(self):
        pass
    
    # Dog 클래스는 부모 클래스 Animal의 기능을 그대로 사용할 수 있습니다.
    # 추가로 특별한 기능을 정의하지 않았기 때문에 부모 클래스의 속성과 메서드를 물려받기만 합니다.
    
class Cat(Animal):
    def __init__(self):
        pass
    
    def walking(self, legs):
        return f'{legs}로 걷는다'
    
    def speak(self, species):
        return f'{species} species!'
    
    # Cat 클래스는 부모 클래스의 __init__() 메서드를 그대로 사용하지만, 새로운 메서드 walking()을 추가했습니다.
    # 또한 부모 클래스의 speak() 메서드를 재정의(override)하여 다른 동작을 하도록 변경했습니다.    
    
if __name__=='__main__':
    # dog = Dog()
    cat = Cat()
    cat.speak('Cat')
    cat.walking('4')
    pass
'''
1. cat = Cat()
    Cat 클래스의 객체(인스턴스)를 생성합니다.
    부모 클래스 Animal의 초기화 메서드(__init__)를 상속받았으므로, 이름 기본값은 'JuJu'입니다.

2. cat.speak('Cat')
    자식 클래스 Cat의 speak() 메서드를 호출합니다.
    부모 클래스에서 물려받은 speak() 대신, 재정의된 메서드가 실행되어 결과는 "Cat species!"입니다.

3. cat.walking('4')
    자식 클래스에서 새롭게 추가된 메서드 walking()을 호출합니다.
    결과는 "4로 걷는다"입니다.
'''