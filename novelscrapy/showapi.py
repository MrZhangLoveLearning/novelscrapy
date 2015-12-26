# -*- coding: utf-8 -*-
# @Date    : 2015-12-26 23:29:56
# @Author  : Zhang Lun (2529450174@qq.com)
# @Link    : https://github.com/MrZhangLoveLearning
from flask import Flask
from flask import request
from  qiniu import Auth,put_file,put_data
from qiniu import BucketManager
import requests
import connection
import run
app = Flask(__name__)
app.debug=True
access_key='QMFf5N9UEXGQfo--ffTjYP7zAvwf6yojVQaCq-um'
secret_key='xs3NHWFAMUfXVs8pFlOewA4E4M3BNzsFpN-j-pqd'
bucket_name='testqiniuyun'
@app.route('/')
def hello_world():
    text = run.get_text()
    return text

@app.route('/update', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        q=Auth(access_key,secret_key)
        buck=BucketManager(q)

        token=q.upload_token(bucket_name)
        key='testDB.db'
        mime_type='text/plain'
        f = request.files['file']
        data=f.read()
        file_path=connection.base_dir+'testDB.db'
        localfile=file_path
        ret,info=put_data(token,key,data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8585)
