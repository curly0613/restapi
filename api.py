# -*- coding: utf-8 -*-
from fastapi import Request, UploadFile, File, Form
from util.errorhandler import *
from util import utils
from util.set import app

from models.models import Model


@app.on_event("startup")
async def startup_event() :
    # API 시작 전 실행할 동작 작성
    global model
    model = Model()

@app.on_event("shutdown")
async def shutdown_event():
    # API 종료 전 실행할 동작 작성
    print("Server shutdown")


# GET METHOD
@app.get("/test_0")
async def test_0() :
    output_json = {'results' : 'Done'}
    return output_json

# POST METHOD
@app.post("/test_1")
async def test_1(request:Request) :
    # preprocessing
    input_json = utils.preproc(await request.json())

    # run processing
    output_json = model.recog(input_json)

    return utils.postproc(output_json)

# 이미지 파일 수신
@app.post("/test_2")
async def test_2(args1:int=Form(...), args2:UploadFile=File(...)) :
    # preprocessing
    input_json = utils.preproc(args1)
    if not input_json :
        raise decodeError()

    # file save
    if not utils.save_image(args2.file.read(), 'temp.png') :
        raise fileSaveError()
    
    # run processing
    output_json = model.recog(input_json)
    if not output_json :
        raise modelError()

    return utils.postproc(output_json)