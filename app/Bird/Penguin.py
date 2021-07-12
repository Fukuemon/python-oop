'''
Created on 2018/10/05

@author: naoki_okada
'''

from .SwimBird import SwimBird
from .SwimFast import SwimFast
from .SwimSlow import SwimSlow

class Penguin(SwimBird):
    '''
    ペンギンを定義する
    クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''
        '''
        SwimBirdクラスから継承した
        _fly_objプロパティにSwimFast
        インスタンスを入れる
        '''
        self._swim_obj = SwimFast()
