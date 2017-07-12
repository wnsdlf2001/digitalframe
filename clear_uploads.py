# -*- coding: utf-8 -*-
"""clear_uplaods.py

This module's name is 'clear_uplaods'.
This module will remove all contents in a specific directory.

"""
import shutil
import os
import constant

# main function
if __name__ == "__main__":
    shutil.rmtree(os.getcwd() + os.sep + constant.CONST_UPLOAD_DIR_NAME, ignore_errors=True)
    print('Clear all files in an upload directory...')
