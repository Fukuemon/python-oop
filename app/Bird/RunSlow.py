'''
Created on 2018/10/05

@author: naoki_okada
'''

from .RunAction import RunAction

class RunSlow(RunAction):
    '''
    遅く走る
    クラスを定義する
    '''


    def run(self):
        print('遅く走る')