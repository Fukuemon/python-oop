'''
Created on 2018/10/04

@author: naoki_okada
'''

from .FlyAction import FlyAction

class FlyNormal(FlyAction):
    '''
    普通に飛ぶ
    クラスを生成する
    '''

    def fly(self):
        print("普通に飛ぶ")
