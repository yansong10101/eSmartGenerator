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
            self.att_dict = dicts['attributes']
            for item in dicts.values():
                if item is not None:
                    print(item)

    def write_regular(self):
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + self.formName + Constants.FILE_EXTENSION_REGULAR
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
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + self.formName + Constants.FILE_EXTENSION_METHOD
        if not os.path.isfile(Constants.SOURCE_FILE_PATH_METHOD):
            return 'no source file exist'
        if not os.path.isdir(Constants.SOURCE_FILE_PATH_DESTINATION):
            os.mkdir(Constants.SOURCE_FILE_PATH_DESTINATION)
        file_source = open(Constants.SOURCE_FILE_PATH_METHOD, 'r').read()
        file_regular = open(obj_file_path, 'w+')
        file_regular.write(Template(file_source).substitute({'formName': self.formName}))
        print('finish generating' + self.formName + '.method.cs file')

    def write_properties(self):
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + self.formName + \
            Constants.FILE_EXTENSION_PROPERTIES
        if not os.path.isfile(Constants.SOURCE_FILE_PATH_PROPERTIES):
            return 'no source file exist'
        if not os.path.isdir(Constants.SOURCE_FILE_PATH_DESTINATION):
            os.mkdir(Constants.SOURCE_FILE_PATH_DESTINATION)
        file_source = open(Constants.SOURCE_FILE_PATH_PROPERTIES, 'r').read()
        file_regular = open(obj_file_path, 'w+')
        # test write insertion point block
        insert_private_block = '\n\t\t'.join(DynamicModule.properties_private_module(self.att_dict))
        insert_access_block = '\n\t\t'.join(DynamicModule.properties_accessories_module(self.att_dict))
        dc = {'formName': self.formName,
              Constants.DYNAMIC_BLOCK_PROPERTIES_PRIVATE: insert_private_block,
              Constants.DYNAMIC_BLOCK_PROPERTIES_ACCESS: insert_access_block}
        file_regular.write(Template(file_source).substitute(dc))
        print('finish generating' + self.formName + '.properties.cs file')

    def write_dao(self):
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + self.formName + Constants.FILE_EXTENSION_DAO
        if not os.path.isfile(Constants.SOURCE_FILE_PATH_DAO):
            return 'no source file exist'
        if not os.path.isdir(Constants.SOURCE_FILE_PATH_DESTINATION):
            os.mkdir(Constants.SOURCE_FILE_PATH_DESTINATION)
        file_source = open(Constants.SOURCE_FILE_PATH_DAO, 'r').read()
        file_regular = open(obj_file_path, 'w+')
        file_regular.write(Template(file_source).substitute({'formName': self.formName}))
        print('finish generating' + self.formName + 'DAO.cs file')

    def write_dao_method(self):
        obj_file_path = Constants.SOURCE_FILE_PATH_DESTINATION + '\\' + self.formName + \
            Constants.FILE_EXTENSION_DAO_METHOD
        if not os.path.isfile(Constants.SOURCE_FILE_PATH_DAO_METHOD):
            return 'no source file exist'
        if not os.path.isdir(Constants.SOURCE_FILE_PATH_DESTINATION):
            os.mkdir(Constants.SOURCE_FILE_PATH_DESTINATION)
        file_source = open(Constants.SOURCE_FILE_PATH_DAO_METHOD, 'r').read()
        file_regular = open(obj_file_path, 'w+')
        # initialize dao.method.cs dynamic block contents
        insert_const_block = '\n\t\t'.join(DynamicModule.dao_method_public(self.att_dict))
        insert_field_block = '\n\t\t\t\t'.join(DynamicModule.dao_method_sql_insert_field(self.att_dict))
        insert_value_block = '\n\t\t\t\t'.join(DynamicModule.dao_method_sql_insert_value(self.att_dict))
        insert_update_block = '\n\t\t\t\t'.join(DynamicModule.dao_method_sql_update(self.att_dict))
        insert_fill_block = '\n\t\t\t'.join(DynamicModule.dao_method_fill(self.att_dict, self.formName))
        insert_save_block = '\n\t\t\t\t'.join(DynamicModule.dao_method_save(self.att_dict, self.formName))
        insert_setup_block = '\n\t\t\t'.join(DynamicModule.dao_method_setup(self.att_dict))
        dc = {'formName': self.formName,
              Constants.DYNAMIC_BLOCK_DAO_PUBLIC_CONST: insert_const_block,
              Constants.DYNAMIC_BLOCK_DAO_INSERT_FIELD: insert_field_block,
              Constants.DYNAMIC_BLOCK_DAO_INSERT_VALUE: insert_value_block,
              Constants.DYNAMIC_BLOCK_DAO_UPDATE: insert_update_block,
              Constants.DYNAMIC_BLOCK_DAO_FILL: insert_fill_block,
              Constants.DYNAMIC_BLOCK_DAO_SAVE: insert_save_block,
              Constants.DYNAMIC_BLOCK_DAO_SETUP: insert_setup_block}
        file_regular.write(Template(file_source).substitute(dc))
        print('finish generating' + self.formName + 'DAO.method.cs file')