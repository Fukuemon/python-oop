'''
Created on 2018/10/05

@author: naoki_okada
'''

from abc import ABCMeta, abstractproperty, abstractmethod

class SwimAction(metaclass=ABCMeta):
    '''
    泳ぐ 動作を処理する
    インターフェース
    ・SwimFast.py(速く泳ぐ）
    ・SwimSlow.py（遅く泳ぐ）
    のインターフェースとして定義
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''
        pass

    def swim(self):
        pass
