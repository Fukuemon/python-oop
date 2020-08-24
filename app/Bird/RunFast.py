'''
Created on 2018/10/05

@author: naoki_okada
'''

from .RunAction import RunAction

class RunFast(RunAction):
    '''
    速く走る
    クラスを定義する
    '''

    def run(self):
        print('速く走る')
