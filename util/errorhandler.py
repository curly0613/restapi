from fastapi import HTTPException

class keyHandler(HTTPException):
    def __init__(self, key):
        self.status_code = 400
        self.error_code = 40100
        self.detail = "'%s' is not in request json keys"%key

    def __str__(self):
        return self.key

class decodeError(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.error_code = 40200
        self.detail = "Image File is not Base64 Encode Format"

class fileSaveError(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.error_code = 40300
        self.detail = "Image File broken"

class modelError(HTTPException):
    def __init__(self):
        self.status_code = 500
        self.error_code = 50100
        self.detail = "Model Error"
