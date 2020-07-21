'''
以下にpythonで処理を書く
'''
import os,sys

''' フルネームを取得する'''
def get_full_name(first_name, family_name):
    return str(family_name) + str(first_name)

print(get_full_name('直己', '岡田'))