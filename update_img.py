# -*- coding: utf-8 -*-
"""update_img.py

This module's name is 'update_img'.
This module will download images in a specific directory of Dropbox.

"""
import subprocess
from syncmanager import SyncMananger
import constant


def GIF():
    fm = SyncMananger(constant.CONST_TOKEN)
    isChanged = fm.downloads(dropbox_path=constant.CONST_GIFIMG_DIR_NAME, local_path=constant.CONST_LOCAL_GIFIMG_DIR_NAME)
    
def pic():
    fm = SyncMananger(constant.CONST_TOKEN)
    isChanged2 = fm.downloads(dropbox_path=constant.CONST_IMG_DIR_NAME, local_path=constant.CONST_LOCAL_IMG_DIR_NAME)

