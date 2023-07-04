'''
Created on 2018/09/13

@author: naoki_okada
'''
from abc import ABCMeta, abstractproperty, abstractmethod

class PersonAbstract(metaclass=ABCMeta):
    '''
    人間の抽象クラス
    抽象クラスは、インスタンス化できない
    概念をまとめた、基本的な処理を定義して
    継承するクラスの挙動を統一する
    '''
    
    def __init__(self, first_name = None, family_name = None):
        self.first_name     = first_name
        self.family_name    = family_name
        self.full_name      = None
 
 # -------------------------------------------
    #ここで先に作りたい関数の土台を作っておく
    
    #フルネームを返す
    @abstractmethod
    def get_full_name(self):
        pass

    #挨拶をする
    @abstractmethod
    def say_hello(self):
        pass

    #さよならを言う
    @abstractmethod
    def say_goodby(self):
        pass
    
    #これらの関数を元に、継承して日本とアメリカの仕様に合わせた関数を作っていく