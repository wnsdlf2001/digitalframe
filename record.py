# -*- coding: utf-8 -*-
"""record.py

This module's name is 'record'.
This module will record using Picamera & upload a recorded video to Dropbox.

"""
from picamera import PiCamera
import datetime
import os
from time import sleep

from syncmanager import SyncMananger
import constant

# main function
if __name__ == "__main__":

    file_name = constant.CONST_UPLOAD_DIR_NAME + os.sep + \
                datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f') + '.h264'

    with PiCamera() as camera:
        camera.resolution = (constant.CONST_CAMCORDER_RESOLUTION_MAX_WIDTH, \
                             constant.CONST_CAMCORDER_RESOLUTION_MAX_HEIGHT)
        camera.framerate = constant.CONST_CAMCORDER_FRAMERATE
        camera.start_recording(file_name)
        sleep(constant.CONST_CAMCORDER_RECORDING_TIME)
        camera.stop_recording()

    fm = SyncMananger(constant.CONST_TOKEN)
    fm.uploads(local_path=constant.CONST_UPLOAD_DIR_NAME, dropbox_path=constant.CONST_UPLOAD_DIR_NAME)
