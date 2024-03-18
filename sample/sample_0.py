# -*- coding: utf-8 -*-
import time
import requests

if __name__ == "__main__" :
    #s_time = time.time()
    res = requests.get("http://0.0.0.0:9999/test_0")

    #print(time.time()-s_time)
    print(res.json())

