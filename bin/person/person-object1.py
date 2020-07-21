# -*- coding: utf-8 -*-

'''
人間情報を扱うサンプルプログラム
クラス利用
'''

import os
import sys

if __name__ == '__main__':
    path = os.path.normpath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '../../'
    ))
    sys.path.append(path)

    from app.Person.Single import SingleSample
    #インスタンス化
    obj = SingleSample()
    #名前の設定
    obj.first_name  = '直己'
    obj.family_name = '岡田'
    #フルNameの取得
    full_name       = obj.get_full_name()
    print(full_name)