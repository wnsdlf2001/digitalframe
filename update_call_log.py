# -*- coding: utf-8 -*-
"""update_img.py

This module's name is 'update_call_log'.
This module will upadate call log and check in a specific directory of Dropbox.

"""
import subprocess
from syncmanager import SyncMananger
import constant


def CallLog():
    fm = SyncMananger(constant.CONST_TOKEN)
    isChanged = fm.downloads(dropbox_path=constant.CONST_CALL_LOG, local_path=constant.CONST_CALL_LOG)


