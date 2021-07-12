'''
Created on 2018/10/05

@author: naoki_okada
'''

from .Abstract import BirdAbstract
from abc import ABCMeta, abstractproperty, abstractmethod

class RunBird(BirdAbstract,metaclass=ABCMeta):
    '''
    走る鳥の種類の
    抽象クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

        '''走るインスタンスを格納
        する為に定義
        '''
        self._run_obj = None

    def run(self):
        '''走るメソッド'''
        self._run_obj.run()