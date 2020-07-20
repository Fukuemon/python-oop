'''
Created on 2018/09/14
Update 2020/07/09
@author: naoki_okada
'''
from .Abstract import PersonAbstract
from .Job import Job

class Japanese(PersonAbstract, Job):
    '''
    日本人を扱うクラス
    '''

    country = 'Japan'

    def __init__(self, first_name = None, family_name = None):
        '''
        コンストラクタ
        '''
        super().__init__(first_name, family_name)
        self._access      = 1
        self.__no_acccess = 2

    def get_full_name(self):
        '''
        フルネームを取得する
        '''
        self.full_name = str(self.family_name) + str(self.first_name)
        return self.full_name

    def say_hello(self):
        '''
        挨拶をする
        オーバーライド
        '''
        print('こんにちは')
        self.teacher()

    def say_goodby(self):
        '''
        さよならを言う
        オーバーライド
        '''
        print('さようなら')