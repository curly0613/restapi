import json


def init_config(config_path) :
    cfg = dict()
    with open(config_path) as rf :
        cfg = json.load(rf)

    return dotdict(cfg)

class dotdict(dict) :
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
