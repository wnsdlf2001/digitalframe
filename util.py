# -*- coding: utf-8 -*-
"""util.py

This module's name is 'util'.
This module is utility to use in the piframe.

"""
import os


def convert_directory_separator(path):
    """Convert the directory separator. '\' --> '/' 
    
    Args:
        path (str): directory path

    Returns:
        Converted directory path

    """
    if os.path.sep != '/':
        path = path.replace(os.path.sep, '/')

    return '/' + path
    

def get_unicode(text):
    """Get a converted unicode value.
    
    Args:
        test (str): Text to be converted.

    Returns:
        Converted text to unicode.

    """
    ret = text

    try:
        ret = text.decode('utf-8')
    except UnicodeDecodeError:
        print( '** UnicodeDecodeError')

        try:
            ret = text.decode('cp949')
        except UnicodeDecodeError:
            print ('** UnicodeDecodeError... I cannot decode...')
    
    return ret
