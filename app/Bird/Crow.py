'''
Created on 2023/07/04
@author: Fukuura Yuya
'''
from .Abstract import BirdAbstract

class Crow(BirdAbstract):
    '''
    カラスを扱うクラス
    BirdAbstractクラスを継承している
    '''
    
    def __init__(self, name):
        '''
        コンストラクタ
        '''
        
        super().__init__(name)
        self._access       = 1
        self.__no_acccess  = 2
        
    def sing(self):
        print('sing:鳴く')
    
    def eat(self):
        print('eat:食べる')
    
    def fly(self):
        print('fly:飛ぶ')