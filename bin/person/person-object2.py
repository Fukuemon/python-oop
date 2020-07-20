# -*- coding: utf-8 -*-

'''
人間情報を扱うサンプルプログラム
クラス利用

ポリモーフィズム
'''

import os,sys

if __name__ == '__main__':
    path = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),'../../'))
    sys.path.append(path)

    from app.Person.Japanese import Japanese
    #from app.Person.American import American
    obj = Japanese()
    #obj = American()
    #first_nameを設定
    obj.first_name = '直己'
    #family_nameを設定
    obj.family_name = '岡田'
    full_name = obj.get_full_name()
    print(full_name)
    obj.say_hello()