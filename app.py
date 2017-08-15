import json
import os
import time

from flask import Flask
from flask import request
from flask import send_from_directory
from PIL import Image
from CaptchaSolver import *


app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 # max file 2mb

ALLOWED_EXTENSIONS = set(['jpg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/.well-known/pki-validation/fileauth.txt', methods=['GET'])
def download():
    return send_from_directory('.', "fileauth.txt", as_attachment=True)

@app.route('/jwc', methods=['POST'])
def jwc():
    response = {'succeed': 0}
    try:
        captcha_file = request.files['captcha']
    except Exception as e:
        response['reason'] = "cannot fetch the image file, please post it with key 'captcha'."
        return json.dumps(response)

    if not allowed_file(captcha_file.filename):
        response['reason'] = "this file type is no supported."
        return json.dumps(response)

    try:
        im = Image.open(captcha_file)
        predict = solve_jwc(im)
    except Exception as e:
        response['reason'] = "an error occurred: %s" % str(e)
    else:
        response['succeed'] = 1
        response['result'] = predict
    return json.dumps(response)


@app.route('/phylab', methods=['POST'])
def phylab():
    response = {'succeed': 0}
    try:
        captcha_file = request.files['captcha']
    except Exception as e:
        response['reason'] = "cannot fetch the image file, please post it with key 'captcha'."
        return json.dumps(response)

    if not allowed_file(captcha_file.filename):
        response['reason'] = "this file type is no supported."
        return json.dumps(response)

    try:
        im = Image.open(captcha_file)
        predict = solve_phylab(im)
    except Exception as e:
        response['reason'] = "an error occurred: %s" % str(e)
    else:
        response['succeed'] = 1
        response['result'] = predict
    return json.dumps(response)


@app.route('/xgb', methods=['POST'])
def xgb():
    response = {'succeed': 0}
    try:
        captcha_file = request.files['captcha']
    except Exception as e:
        response['reason'] = "cannot fetch the image file, please post it with key 'captcha'."
        return json.dumps(response)

    if not allowed_file(captcha_file.filename):
        response['reason'] = "this file type is no supported."
        return json.dumps(response)

    try:
        filename = time.time()
        captcha_file.save("tmp/%s" % (str(filename)))
        cmd = "tesseract tmp/%s stdout" % (filename)
        predict = str(os.popen(cmd).read().strip('\n'))

        os.popen("mv tmp/%s tmp/%s" % (str(filename), "".join([str(filename), "_", predict])))
    except Exception as e:
        response['reason'] = "an error occurred: %s" % str(e)
    else:
        response['succeed'] = 1
        response['result'] = predict
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')