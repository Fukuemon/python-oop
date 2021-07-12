'''
Created on 2018/10/03

@author: naoki_okada
'''
from abc import ABCMeta, abstractproperty, abstractmethod

class BirdAbstract(metaclass=ABCMeta):
    '''
    鳥を扱う抽象クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''
        pass

    def eat(self):
        '''エサを食べるメソッド'''
        print("エサを食べる")

    def sing(self):
        '''鳴くメソッド'''
        print("鳴く")