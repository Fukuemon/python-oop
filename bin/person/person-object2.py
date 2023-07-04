# -*- coding: utf-8 -*-

'''
人間情報を扱うサンプルプログラム
クラス利用

ポリモーフィズム
'''

import os,sys

if __name__ == '__main__':
# ----------------------------------------------
    #パスを通してパッケージを読み込む
    path = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),'../../'))
    sys.path.append(path)

    from app.Person.Japanese import Japanese
    from app.Person.American import American
# ----------------------------------------------
    obj_jp = Japanese()
    obj_am = American()
    #first_nameを設定
    obj_jp.first_name = '太郎'
    obj_am.first_name = 'Taro'
    #family_nameを設定
    obj_jp.family_name = '山田'
    obj_am.family_name = 'Yamada'
    full_name_jp = obj_jp.get_full_name()
    full_name_am = obj_am.get_full_name()
    print('日本人:' + full_name_jp)
    print('アメリカ人：' + full_name_am)
    #say_helloメソッドを使う
    obj_jp.say_hello()
    obj_am.say_hello()