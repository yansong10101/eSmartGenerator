__author__ = 'yansong'
import genApp.genlib.CommonConstants as Constants
import genApp.genlib.formModules.dynamicModule as DynamicModule
import os
from string import Template
import shutil


class GeneratePIT():

    def __init__(self, dicts):
        if dicts is not None:
            self.dicts = dicts
            self.formName = dicts['formName']
            for item in dicts.values():
                if item is not None:
                    print(item)

    def write_regular(self):
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + \
                        self.formName + Constants.FILE_EXTENSION_REGULAR
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
        file_source = open(Constants.SOURCE_FILE_PATH_REGULAR, 'r').read()
        # create or open exist file in output dir
        file_regular = open(obj_file_path, 'w+')
        # do write with substitution
        file_regular.write(Template(file_source).substitute({'formName': self.formName}))
        print('finish generating' + self.formName + '.cs file')

    def write_method(self):
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + \
                        self.formName + Constants.FILE_EXTENSION_METHOD
        if not os.path.isfile(Constants.SOURCE_FILE_PATH_METHOD):
            return 'no source file exist'
        if not os.path.isdir(Constants.SOURCE_FILE_PATH_DESTINATION):
            os.mkdir(Constants.SOURCE_FILE_PATH_DESTINATION)
        file_source = open(Constants.SOURCE_FILE_PATH_METHOD, 'r').read()
        file_regular = open(obj_file_path, 'w+')
        file_regular.write(Template(file_source).substitute({'formName': self.formName}))
        print('finish generating' + self.formName + '.method.cs file')

    def write_properties(self):
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + \
                        self.formName + Constants.FILE_EXTENSION_PROPERTIES
        print('source file from :' + Constants.SOURCE_FILE_PATH_PROPERTIES)
        print('generate file to :' + obj_file_path)
        # check source and destination dir
        if not os.path.isfile(Constants.SOURCE_FILE_PATH_PROPERTIES):
            # return if no source template
            return 'no source file exist'
        if not os.path.isdir(Constants.SOURCE_FILE_PATH_DESTINATION):
            # if not exist, create a new output folder
            os.mkdir(Constants.SOURCE_FILE_PATH_DESTINATION)
        # read source file
        file_source = open(Constants.SOURCE_FILE_PATH_PROPERTIES, 'r').read()
        # create or open exist file in output dir
        file_regular = open(obj_file_path, 'w+')
        dc = {'formName': self.formName,
              'dynamic_module_data_member': 'dynamic_module_data_member',
              'dynamic_module_access': 'dynamic_module_access'}
        file_regular.write(Template(file_source).substitute(dc))
        print('finish generating' + self.formName + '.properties.cs file')

    def write_dao(self):
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + \
                        self.formName + Constants.FILE_EXTENSION_DAO
        if not os.path.isfile(Constants.SOURCE_FILE_PATH_DAO):
            return 'no source file exist'
        if not os.path.isdir(Constants.SOURCE_FILE_PATH_DESTINATION):
            os.mkdir(Constants.SOURCE_FILE_PATH_DESTINATION)
        file_source = open(Constants.SOURCE_FILE_PATH_DAO, 'r').read()
        file_regular = open(obj_file_path, 'w+')
        file_regular.write(Template(file_source).substitute({'formName': self.formName}))
        print('finish generating' + self.formName + 'DAO.cs file')

    def write_dao_method(self):
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + \
                        self.formName + Constants.FILE_EXTENSION_DAO_METHOD
        # check source and destination dir
        if not os.path.isfile(Constants.SOURCE_FILE_PATH_DAO_METHOD):
            # return if no source template
            return 'no source file exist'
        if not os.path.isdir(Constants.SOURCE_FILE_PATH_DESTINATION):
            # if not exist, create a new output folder
            os.mkdir(Constants.SOURCE_FILE_PATH_DESTINATION)
        # read source file
        file_source = open(Constants.SOURCE_FILE_PATH_DAO_METHOD, 'r')
        # create or open exist file in output dir
        file_regular = open(obj_file_path, 'w+')
        # read lines from source template file
        file_lines = file_source.readlines()
        for file_line in file_lines:
            line = file_line.replace('${formName}', self.formName)
            file_regular.writelines(line)
        print('finish generating' + self.formName + 'DAO.method.cs file')