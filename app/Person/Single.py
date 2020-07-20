'''
Created on 2018/09/14
@author: naoki_okada
'''
class SingleSample():
    ''' サンプルの単体クラス'''

    def __init__(self, first_name = None, family_name = None):
        ''' コンストラクタ '''
        self.first_name  = first_name
        self.family_name = family_name
        self.full_name   = None

    def get_full_name(self):
        ''' フルネームを取得する '''
        self.full_name = str(self.family_name) + str(self.first_name)

        return self.full_name