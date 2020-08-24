'''
Created on 2018/10/05

@author: naoki_okada
'''

from .SwimAction import SwimAction

class SwimSlow(SwimAction):
    '''
    遅く泳ぐ
    クラスを定義する
    '''

    def swim(self):
        print("遅く泳ぐ")