# -*- coding: utf-8 -*-
import time
import requests

if __name__ == "__main__" :
    input_json = dict()
    input_json['args1'] = 1

    #s_time = time.time()
    res = requests.post("http://0.0.0.0:9999/test_1", json=input_json)

    #print(time.time()-s_time)
    print(res.json())

