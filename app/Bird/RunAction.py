'''
Created on 2018/10/05

@author: naoki_okada
'''
from abc import ABCMeta, abstractproperty, abstractmethod

class RunAction(metaclass=ABCMeta):
    '''
    走る 動作を処理する
    インターフェース
    ・RunFast.py(速く走る）
    ・RunSlow.py（遅く走る）
    のインターフェースとして定義
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''
        pass

    def run(self):
        pass