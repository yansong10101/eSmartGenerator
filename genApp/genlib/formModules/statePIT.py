__author__ = 'yansong'
import genApp.genlib.CommonConstants as Constants
import os
import shutil
from string import Template


class GeneratePIT():

    def __init__(self, dictquarter):
        if dictquarter is not None:
            self.dictQuarter = dictquarter
            self.formName = dictquarter['formName']
            for item in dictquarter.values():
                if item is not None:
                    print(item)

    def write_regular(self):
        obj_name = self.formName
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + obj_name + Constants.FILE_EXTENSION_REGULAR
        print('source file from :' + Constants.SOURCE_FILE_PATH_REGULAR)
        print('generate file to :' + obj_file_path)
        # check source and destination dir
        if not os.path.isfile(Constants.SOURCE_FILE_PATH_REGULAR):
            # return if no source template
            return 'no source file exist'
        if not os.path.isdir(Constants.SOURCE_FILE_PATH_DESTINATION):
            # if not exist, create a new output folder
            os.mkdir(Constants.SOURCE_FILE_PATH_DESTINATION)
        # read source file
        file_source = open(Constants.SOURCE_FILE_PATH_REGULAR, 'r')
        # create or open exist file in output dir
        file_regular = open(obj_file_path, 'w+')
        # read lines from source template file
        file_lines = file_source.readlines()
        for file_line in file_lines:
            line = file_line.replace('${name}', obj_name)
            file_regular.writelines(line)
        print('finish generating')