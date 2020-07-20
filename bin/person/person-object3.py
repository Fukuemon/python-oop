# -*- coding: utf-8 -*-

'''
人間情報を扱うサンプルプログラム
クラス利用

インスタンス変数 と クラス変数
カプセル化
'''

import os,sys

if __name__ == '__main__':
    path = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),'../../'))
    sys.path.append(path)

    from app.Person.Japanese import Japanese
    obj  = Japanese()
    obj2 = Japanese()
    obj.first_name  = '名前1'
    obj2.first_name = '名前2'

    #'''
    #インスタンス変数はそれぞれ、違う管理になる
    print(obj.first_name)
    print(obj2.first_name)
    #'''

    '''
    #クラス変数は、クラスごとに管理される
    print(obj.country)
    #クラス変数の更新
    Japanese.country = 'U.S.A'
    #すべてのインスタンスに影響
    print(obj2.country)
    '''

    #アクセス可能なインスタンス変数
    #print(obj._access)

    #アクセス不可能なインスタンス変数
    #print(obj.__no_access)

    #dirでインスタンスの中身を見る
    #マングリングされているのがわかる
    #print(dir(obj))