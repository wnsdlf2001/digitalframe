# -*- coding: utf-8 -*-
"""syncmanager.py

This module's name is 'syncmanager'.
This module synchronizes your local storage with a specific path of Dropbox.

"""

import os
import sys
import util
import shutil
import dropbox
from dropbox.files import FolderMetadata 
from dropbox.files import Metadata


class SyncMananger(object):
    """This SyncManager class synchronizes your local storage with Dropbox.
    
    If you want to use this class, you should have a OAuth2 access key of your application.
    You can generate one for yourself in the App Console.

    """


    def __init__(self, token):
        """constructor

        Args:
            token (str): the OAuth 2 access token of an application.  

        """
        self._dbx = dropbox.Dropbox(token)
        # Check that the access token is valid
        try:
            self._dbx.users_get_current_account()

        except:
            sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
        #except AuthError as err:
        #    sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")


    def downloads(self, dropbox_path='/', local_path='.'):
        """downloads

        You can synchronize Dropbox files to a local storage.

        Args:
            dropbox_path (str): The directory path in a dropbox
            local_path (str): The directory path in a local storage

        Returns:
            isChanged (boolean): If it has changed items, this api will return True.
        """
        isChanged = False
        local = self._get_files_dict(local_path)
        online = self._get_files_dict('/' + dropbox_path, isonline=True)

        online_keys = online.keys()
        online_vals = online.values()

        #print('*** local keys : ', local.keys())
        #print('*** local values : ', local.values())
        #print('*** online keys : ', online_keys)
        #print('*** online values : ', online.values())

        for i in range(0, len(online_keys)):
            try:
                if (local.has_key(online_keys[i])):
                    if (self._is_same(online_vals[i], local[online_keys[i]])):
                        local.pop(online_keys[i])
                        online.pop(online_keys[i])

            except KeyError:
                pass

        #The reminder of online will be downloaded.
        downloaded_files = self._download_files(online)
        for i in range(0, len(downloaded_files)):
            try:
                local.pop(downloaded_files[i])

            except KeyError:
                pass
    
        #The reminder of local will be deleted.
        self._remove_files(local)
        print('*** downloads is complete.')

        if len(downloaded_files) > 0 or len(local) > 0:
            isChanged = True

        return isChanged


    def _is_same(self, dropbox_metadata, local_file_name):
        """Check difference between a file in dropbox and a local file. 
        
        Args:
            dropbox_metadata (dropbox.files.Metadata): Metadata
            local_file_name (str): file name on a local storage

        Returns:
            Ture if same, False otherwise.

        """
        if (isinstance(dropbox_metadata, Metadata) is not True):
            return False
        elif (isinstance(dropbox_metadata, FolderMetadata)):
            return True
        elif (dropbox_metadata.size != os.path.getsize(local_file_name)):
            return False
        
        return True

    
    def _remove_files(self, dict_files):
        """Remove files in the dict on a local storage.

        Args:
            dict_files (dict): The dictionary has files to be removed.

        """
        for k, v in dict_files.items():

            try:
                file_path = os.getcwd() + k.replace('/', os.sep)
                
                if (os.path.isdir(file_path)):
#                    os.rmdir(file_path)
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)

            except Exception:
                print('*** Error')
                pass
                

    def _download_files(self, dict_files):
        """Download files in Dropbox to a local storage.
        
        Args:
            dict_files (dict): The dictionary has files to be downloaded.

        Returns:
            The list of downloaded files

        """
        rets = []

        for k, v in dict_files.items():
            try:
                file_path = os.getcwd() + k.replace('/', os.sep)

                if not os.path.exists(os.path.dirname(file_path)):
                    os.makedirs(os.path.dirname(file_path))

                if (isinstance(v, FolderMetadata)):
                    continue

                print ('*** downloading... to ' + os.getcwd() + k.replace('/', os.sep))
                self._dbx.files_download_to_file(file_path, k)
                print ('downloaded the ' + k)
                rets.append(k)

            except dropbox.exceptions.HttpError as derr:
                print('*** HTTP error', derr)
            except IOError as ioerr:
                print('*** IO error', ioerr)
            except BaseException:
                print('*** Unkwon error')
                
        return rets


    def _get_files_dict(self, dir, isonline=False):
        """Get a dictionary that has files.

        Args:
            dir (str): The directory path.
            isonline (bool): True if online, otherwise False

        Returns:
            The dictionary of files

        """
        if (isonline):
            return self._get_dropbox_files_dict(dir)
        else:
            return self._get_local_files_dict(dir)


    def _get_dropbox_files_dict(self, directory='/'):
        """Get a dictionary has files in Dropbox.

        Args:
            directory (str): The directory path in Dropbox.

        Returns:
            The dictionary of Dropbox files.

        """
        files_dict = {}  # Dictionary which will store all of the full filepaths.
        
        print ('*** dropbox files ***')
        try:
            self._dbx.files_create_folder(directory)
        except dropbox.exceptions.ApiError:
            pass

        for entry in self._dbx.files_list_folder(directory, recursive=True).entries:
            files_dict.update({entry.path_display : entry})
            print( '* ' + entry.path_display)

        return files_dict


    def _get_local_files_dict(self, dir='.'):
        """Get a dictionary has files in the local storage.

        Args:
            dir (str): The directory path in the local storage.

        Returns:
            The dictionary of local files.
            
        """
        files_dict = {}  # Dictionary which will store all of the full filepaths.
        
        print( '*** local files ***')
        if not os.path.exists(dir):
            os.makedirs(dir)

        # Walk the tree.
        for root, directories, files in os.walk(dir):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                print ('* ' + filepath)
                files_dict.update({util.get_unicode(util.convert_directory_separator(filepath)) : filepath})  # Add it to the list.
                
            for directory in directories:
                dirpath = os.path.join(root, directory)
                print( '* ' + dirpath)
                files_dict.update({util.get_unicode(util.convert_directory_separator(dirpath)) : dirpath})  # Add it to the list.

        return files_dict  # Self-explanatory.
    

    def uploads(self, local_path='.', dropbox_path='/'):
        """uploads

        You can synchronize local files to dropbox.

        Args:
            local_path (str): The directory path in a local storage
            dropbox_path (str): The directory path in a dropbox            

        """

        local = self._get_files_dict(local_path)
        online = self._get_files_dict('/' + dropbox_path, isonline=True)

        local_keys = local.keys()
        local_vals = local.values()

        #print('*** online keys : ', online.keys())
        #print('*** online values : ', online.values())
        #print('*** local keys : ', local_keys)
        #print('*** local values : ', local_vals)

        for i in range(0, len(local_keys)):
            try:
                if (online.has_key(local_keys[i])):
                    if (self._is_same(online[local_keys[i]], local_vals[i])):
                        local.pop(local_keys[i])
                        online.pop(local_keys[i])

            except KeyError:
                pass

        #The reminder of local will be uploaded.
        uploaded_files = self._upload_files(local)
        print('*** uploads is complete.')


    def _upload_files(self, dict_files):
        """Upload files in a local storage to Dropbox.
        
        Args:
            dict_files (dict): The dictionary has files to be uploaded.

        Returns:
            The list of uploaded files

        """
        rets = []

        for k, v in dict_files.items():
            try:
                file_path = os.getcwd() + k.replace('/', os.sep)
                
                if os.path.isdir(file_path):
                    try:
                        self._dbx.files_create_folder(k)
                        print ('make the directory... ' + k)
                        rets.append(k)
                        continue

                    except dropbox.exceptions.ApiError:
                        continue
                    except BaseException:
                        continue
                # try:
                #     self._dbx.files_create_folder(os.path.dirname(file_path))
                # except dropbox.exceptions.ApiError:
                #     pass
                # except BaseException:
                #     pass
                with open(file_path, 'rb') as f:
                    data = f.read()

                # print '*** uploading... to ' + os.getcwd() + k.replace('/', os.sep)
                self._dbx.files_upload(data, k)
                print ('uploaded the ' + k)
                rets.append(k)

            except dropbox.exceptions.HttpError as derr:
                print('*** HTTP error', derr)
            except dropbox.exceptions.ApiError as aerr:
                print('*** API error', aerr)
            except IOError as ioerr:
                print('*** IO error', ioerr)
            except BaseException:
                print('*** Unkwon error')
                
        return rets



#    def upload(self, file_name, dir_name='', overwrite=False):
#        """Upload a file.
#        
#        Return the request response, or None in case of error.
#        """
#
#        print('dir_name = ', dir_name)
#        print('file_name = ', file_name)
#        print('is overwrite? ', overwrite)
#
#        """mode = (dropbox.files.overwrite
#                if overwrite
#                else dropbox.files.WriteMode.add)
#        """
#
#        file_path = os.getcwd() + os.sep + dir_name + os.sep + file_name
#        try:
#            
#            f = open(file_path, 'r')
#            data = f.read()
#
#            try:
#                res = self.__dbx.files_upload(
#                    data, self.__DIR__ + dir_name + self.__DIR__ + file_name, autorename=True
#                )
#            except dropbox.exceptions.ApiError as err:
#                print('*** API error', err)
#        except IOError:
#            print('*** File open error')
#            return
#
#        print('uploaded as', res.name.encode('utf8'))
#        return res

