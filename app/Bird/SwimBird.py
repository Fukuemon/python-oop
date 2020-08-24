'''
Created on 2018/10/05

@author: naoki_okada
'''

from .Abstract import BirdAbstract
from abc import ABCMeta, abstractproperty, abstractmethod

class SwimBird(BirdAbstract,metaclass=ABCMeta):
    '''
    泳ぐ鳥の種類の
    抽象クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''
        '''泳ぐインスタンスを格納
        する為に定義
        '''
        self._swim_obj = None

    def swim(self):
        '''泳ぐメソッド'''
        self._swim_obj.swim()