'''
Created on 2018/09/14
@author: naoki_okada
'''
from .Abstract import PersonAbstract

class American(PersonAbstract):
    '''
    アメリカ人を扱うクラス
    '''

    country = 'U.S.A'

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
        self.full_name = str(self.first_name) + str(self.family_name)
        return self.full_name

    def say_hello(self):
        '''
        挨拶をする
        オーバーライド
        '''
        print('Hello')

    def say_goodby(self):
        '''
        さよならを言う
        オーバーライド
        '''
        print('Good Bye')