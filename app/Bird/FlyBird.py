'''
Created on 2018/10/04

@author: naoki_okada
'''
from abc import ABCMeta, abstractproperty, abstractmethod
from .Abstract import BirdAbstract

class FlyBird(BirdAbstract,metaclass=ABCMeta):
    '''
    飛ぶ種類の鳥の
    抽象クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

        '''飛ぶインスタンスを格納
        する為に定義
        '''
        self._fly_obj = None

    def fly(self):
        '''継承先のflyで実'''
        self._fly_obj.fly()
