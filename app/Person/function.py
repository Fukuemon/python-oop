'''
Created on 2018/09/14

人物情報モジュール

@author: naoki_okada
'''

''' フルネームを取得する'''
def get_full_name(first_name: str='', family_name: str='') -> str:
    return str(family_name) + str(first_name)