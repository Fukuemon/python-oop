# -*- coding: utf-8 -*-

'''
鳥をオブジェクト指向で
処理する
'''
import os,sys

'''オブジェクトの中身を見る関数'''
def get_object_method(obj):
    for x in dir(obj):
        print(x)

if __name__ == '__main__':
    path = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),'../../'))
    sys.path.append(path)

    from app.Bird.Crow import Crow
    from app.Bird.Ostrich import Ostrich
    from app.Bird.Penguin import Penguin

    first_bird  = Crow()
    second_bird = Ostrich()
    third_bird  = Penguin()

    print('カラス')
    first_bird.eat()
    first_bird.sing()
    first_bird.fly()
    print('-----')

    print('ダチョウ')
    second_bird.eat()
    second_bird.sing()
    second_bird.run()
    print('-----')

    print('ペンギン')
    third_bird.eat()
    third_bird.sing()
    third_bird.swim()