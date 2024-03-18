# -*- coding: utf-8 -*-

class Model : 
    def __init__(self) :
        # 분석 모델 초기화 및 load
        self.model = None

    def recog(self, input_json) :
        try :
            output_json = dict()
            output_json['inputs'] = input_json

            #output_json['results'] = model.recog(args1, args2)
            output_json['results'] = 'done'

            return output_json
        except :
            return False

