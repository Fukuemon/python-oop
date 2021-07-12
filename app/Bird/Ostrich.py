'''
Created on 2018/10/05

@author: naoki_okada
'''

from .RunBird import *
from .RunFast import RunFast
from .RunSlow import RunSlow

class Ostrich(RunBird):
    '''
    ダチョウを定義する
    クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''
        '''
        RunBirdクラスから継承した
        _run_objプロパティにRunFast
        インスタンスを入れる
        '''
        self._run_obj = RunFast()