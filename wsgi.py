# -*- coding: utf-8 -*-
import uvicorn

from util.config import init_config
from api import app

if __name__ == '__main__':
    cfg = init_config('config.json')
    uvicorn.config.LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    uvicorn.config.LOGGING_CONFIG["formatters"]["access"]["fmt"] = '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s' 
    uvicorn.run(app, host=cfg.ip, port=cfg.port)