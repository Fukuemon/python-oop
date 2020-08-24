'''
Created on 2018/10/05

@author: naoki_okada
'''

from .SwimAction import SwimAction

class SwimFast(SwimAction):
    '''
    速く泳ぐ
    クラスを定義する
    '''

    def swim(self):
        print("速く泳ぐ")