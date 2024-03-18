# -*- coding: utf-8 -*-
import time
import requests

if __name__ == "__main__" :
    input_json = dict()
    input_json['args1'] = 1

    #s_time = time.time()
    res = requests.post("http://localhost:9999/test_2", 
                         files={'args2':('sample.png', open('sample.png', 'rb'), 'image/png')}, 
                         data=input_json)

    #print(time.time()-s_time)
    print(res.json())

