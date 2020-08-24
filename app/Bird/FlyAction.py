'''
Created on 2018/10/04

@author: naoki_okada
'''

from abc import ABCMeta, abstractproperty, abstractmethod

class FlyAction(metaclass=ABCMeta):
    '''
    飛ぶ 動作を処理する
    インターフェース
    ・FlyNormal.py(普通に飛ぶ）
    ・FlyHight.py（高く飛ぶ）
    ・FlyLow.py（低く飛ぶ）
    のインターフェースとして定義
    '''

    def fly(self):
        ''' 飛ぶ動作 '''
        pass