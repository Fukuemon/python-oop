'''
Created on 2018/10/05

@author: naoki_okada
'''

from .FlyBird import FlyBird
from .FlyNormal import FlyNormal

class Crow(FlyBird):
    '''
    カラスを定義するクラス
    '''
    def __init__(self):
        '''
        コンストラクタ
        '''
        '''
        FlyBirdクラスから継承した
        _fly_objプロパティにFlyNormal
        インスタンスを入れる
        '''
        self._fly_obj = FlyNormal()