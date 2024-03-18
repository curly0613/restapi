# -*- coding: utf-8 -*-
import base64
import shutil

def preproc(input_json) :
    # input data preprocessing 
    try :

        return input_json
    except :
        return False

def postproc(output_json) :
    # output data postprocessing

    return output_json

def b64encoder(image) :
    return base64.b64encode(image)

def b64decoder(image) :
    return base64.b64decode(image)

def save_image(image, path) :
    try :
        with open(path, 'wb') as wfile :
            wfile.write(image)
        return True
    except :
        return False