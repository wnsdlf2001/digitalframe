# -*- coding: utf-8 -*-
"""capture.py

This module's name is 'capture'.
This module will capture using Picamera & upload a captured pic to Dropbox.

"""
from picamera import PiCamera
import datetime
import os

from syncmanager import SyncMananger
import constant

# main function
if __name__ == "__main__":
    
    if not os.path.exists(constant.CONST_UPLOAD_DIR_NAME):
        os.makedirs(constant.CONST_UPLOAD_DIR_NAME)

    file_name = constant.CONST_UPLOAD_DIR_NAME + os.sep + \
                datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f') + '.jpg'

    with PiCamera() as camera:
        camera.resolution = (constant.CONST_CAMERA_RESOLUTION_MAX_WIDTH, \
                             constant.CONST_CAMERA_RESOLUTION_MAX_HEIGHT)
        camera.capture(file_name)

    fm = SyncMananger(constant.CONST_TOKEN)
    fm.uploads(local_path=constant.CONST_UPLOAD_DIR_NAME, dropbox_path=constant.CONST_UPLOAD_DIR_NAME)
