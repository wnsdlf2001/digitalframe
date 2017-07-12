# -*- coding: utf-8 -*-
"""pidf.py

This module's name is 'pidf'.

"""
#import pika
import subprocess
import json
from flask import Flask
from flask import request
import constant
import madeGUI

app = Flask(__name__)


def process(message='', d=None):

    cmd = message
    param = d
    
    print ('cmd = %r', cmd)
    print ('param = %r', param)

    if cmd == constant.CONST_CMD_COMMAND:
        print('run a command.')
        try:
            command = param.get(constant.CONST_PARAM_COMMAND)
            param1 = param.get(constant.CONST_PARAM_PARAM1)
            param2 = param.get(constant.CONST_PARAM_PARAM2)

            print('command: %r', command)
            print('param1: %r', param1)
            print('param2: %r', param2)

            if param1 is not None and param2 is not None:
                subprocess.call([command, param1, param2])
            elif param1 is not None:
                subprocess.call([command, param1])
        except:
            pass

    elif cmd == constant.CONST_CMD_PYTHON:
        print('run a python script.')
        try:
            param1 = param.get(constant.CONST_PARAM_PARAM1)

            print('param1: %r', param1)
            subprocess.call(['python', param1])
        except:
            pass

    elif cmd == constant.CONST_CMD_WEBHOOKS:
        print('update images in dropbox.')
        subprocess.call(['python', 'update_img.py'])

    else:
        pass
    
    ret = {constant.CONST_CMD: message}
    if d is not None and isinstance(d, dict):
        ret.update({constant.CONST_PARAM: d})

    return json.dumps(ret)


@app.route('/'+constant.CONST_CMD_WEBHOOKS, methods=['GET', 'POST'])
def webhooks():
    ret = process(constant.CONST_CMD_WEBHOOKS)

    if 'challenge' in request.args:
        try:
            
            print('challenge = ',  request.args.get('challenge'))
            ret = request.args.get('challenge')
        except:
            pass

    return ret


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return process(path, request.args.to_dict())
    

if __name__ == '__main__':
    #subprocess.call(['python', 'update_img.py'])
    #subprocess.call(['python', 'play.py'])
    app.run(host='0.0.0.0', debug=True)
    madeGUI()

