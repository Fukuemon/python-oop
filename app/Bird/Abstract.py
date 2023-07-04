'''
Created on 2023/07/09

@author: Fukuura Yuya
'''
from abc import ABCMeta, abstractproperty, abstractmethod

class BirdAbstract(metaclass=ABCMeta):
    """
    鳥の抽象クラス
    """
    
    def __init__(self, name = None):
        self.name = name
        
    
    #鳴く
    @abstractmethod
    def sing(self):
        pass
    
    #餌を食べる
    @abstractmethod
    def eat(self):
        pass
    
