# -*- coding: utf-8 -*-
# @Date    : 2015-12-26 23:29:56
# @Author  : Zhang Lun (2529450174@qq.com)
# @Link    : https://github.com/MrZhangLoveLearning
from flask import Flask
from flask import request

import requests
import connection
import run
app = Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():
    text = run.get_text()
    return text




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2828)
