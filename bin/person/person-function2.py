# -*- coding: utf-8 -*-

'''
人間情報を扱うサンプルプログラム
'''

import os,sys

if __name__ == '__main__':
    path = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),'../../'))
    #includeのパスを追加
    sys.path.append(path)

    import app.Person.function as func
    #from app.Person import function as func
    #from app.Person.function import get_full_name

    first_name    = '直己'
    family_name   = '岡田'

    full_name = func.get_full_name(first_name, family_name)
    #full_name = get_full_name(first_name, family_name)
    print(full_name)