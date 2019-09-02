# -*- coding: utf-8 -*-
"""update_system.py

This module's name is 'update_system'.

"""
import shutil
import os
from syncmanager import SyncMananger
import constant

# main function
if __name__ == "__main__":
    fm = SyncMananger(constant.CONST_TOKEN)
    fm.downloads(constant.CONST_SYSTEM_DIR_NAME, constant.CONST_SYSTEM_DIR_NAME)

    dir_path = os.getcwd() + os.sep + constant.CONST_SYSTEM_DIR_NAME
    for filename in os.listdir(dir_path):
        shutil.copy(dir_path + os.sep + filename, os.getcwd())
