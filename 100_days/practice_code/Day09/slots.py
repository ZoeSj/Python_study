# @File    : slots.py
# @Date    : 2020-09-02
# @Author  : shengjia
"""
是否已经意识到，Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
"""


class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s is playing Ludo.wow it is %s' % (self._name, self._gender))
        else:
            print('%s is play Landlord.wow it is %s' % (self._name, self._gender))


def main():
    person = Person('zoe', 18, 'male')
    person._gender = 'female'
    person.play()


if __name__ == '__main__':
    main()
