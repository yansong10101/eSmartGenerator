__author__ = 'yansong'
import os
import json

# get current file path to open json file in the same directory
json_path = os.path.join(os.path.dirname(__file__), 'ConstantConfig.json')
# open json file and load file contents to 'json_data'
json_file = open(json_path, 'r')
json_data = json.load(json_file)

# json file tag  name
JSON_TOP_NODE_SOURCE_TEMPLATE = 'SourceTemplate'

# Source file template path
SOURCE_FILE_DIR = json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['SrcDir']
SOURCE_FILE_PATH_DESTINATION = json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['DesDir']
SOURCE_FILE_PATH_REGULAR = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['Regular']
SOURCE_FILE_PATH_METHOD = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['Method']
SOURCE_FILE_PATH_PROPERTIES = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['Properties']
SOURCE_FILE_PATH_DAO = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['DAO']
SOURCE_FILE_PATH_DAO_METHOD = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['DAOMethod']

# Lib files extension
FILE_EXTENSION_REGULAR = r'.cs'
FILE_EXTENSION_METHOD = r'.method.cs'
FILE_EXTENSION_PROPERTIES = r'.properties.cs'
FILE_EXTENSION_DAO = r'DAO.cs'
FILE_EXTENSION_DAO_METHOD = r'DAO.method.cs'
FILE_EXTENSION_ASPX = r'.aspx'
FILE_EXTENSION_CS = r'.aspx.cs'

# privilege key words
PRIVILEGE_PRIVATE = 'private'
PRIVILEGE_PROTECTED = 'protected'
PRIVILEGE_PUBLIC = 'public'

# variable prefix
VAR_PREFIX_FRONT_TXT = 'txt_'
VAR_PREFIX_FRONT_CB = 'cb_'
VAR_PREFIX_DATA_MEMBER = 'm_'
VAR_PREFIX_STRING = 's_'
VAR_PREFIX_DOUBLE = 'd_'
VAR_PREFIX_INT = 'i_'
VAR_PREFIX_OBJECT = 'o'
VAR_PREFIX_OBJECT_DASH = 'o_'
VAR_PREFIX_DATETIME = 'dt_'

# form type
FORM_TYPE_PIT_QUARTER = ''
FORM_TYPE_PIT_MONTH = ''
FORM_TYPE_PIT_YEAR = ''
FORM_TYPE_PIT_SEMI_MONTH = ''
FORM_TYPE_UI_QUARTER = ''
FORM_TYPE_UI_YEAR = ''
FORM_TYPE_VOUCHER = ''

# tax properties
TAX_PROPERTIES_EMPLOYER_GID = 'EmployerGID'
TAX_PROPERTIES_EMPLOYER_PROFILE_GID = 'EmployerProfileGID'
TAX_PROPERTIES_EMPLOYER = 'Employer'
TAX_PROPERTIES_EIN = 'EIN'
TAX_PROPERTIES_ACCOUNT_NUMBER = 'AccountNumber'

TAX_PROPERTIES_TAX_YEAR = 'TaxYear'
TAX_PROPERTIES_TAX_MONTH = 'TaxMonth'
TAX_PROPERTIES_TAX_QUARTER = 'TaxQuarter'
TAX_PROPERTIES_TAX_DUE_DATE = 'DueDate'
TAX_PROPERTIES_PERIOD_START = 'PeriodStart'
TAX_PROPERTIES_PERIOD_END = 'PeriodEnd'
TAX_PROPERTIES_MODIFIED_DATE = 'ModifiedDate'

TAX_PROPERTIES_TOTAL_WAGE = 'TotalWage'
TAX_PROPERTIES_TAX_WITHHELD = 'TaxWithheld'
TAX_PROPERTIES_REMITTED = ''
TAX_PROPERTIES_UI_TAX_RATE = ''


def pass_json_to_dict():
    return