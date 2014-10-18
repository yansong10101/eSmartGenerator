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
JSON_TOP_NODE_DAO_TEMPLATE = "DAOTemplate"
JSON_TOP_NODE_DYNAMIC_BLOCK = "DynamicBlockName"

# Source file template path
SOURCE_FILE_DIR = json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['SrcDir']
SOURCE_FILE_PATH_DESTINATION = json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['DesDir']
SOURCE_FILE_PATH_REGULAR = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['Regular']
SOURCE_FILE_PATH_METHOD = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['Method']
SOURCE_FILE_PATH_PROPERTIES = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['Properties']
SOURCE_FILE_PATH_DAO = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['DAO']
SOURCE_FILE_PATH_DAO_METHOD = SOURCE_FILE_DIR + json_data[JSON_TOP_NODE_SOURCE_TEMPLATE]['DAOMethod']

# Files extension
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
VAR_DAO_PREFIX_FIELD = 'FIELD_'

# DAO Method function line template
DAO_FUNCTION_INSERT_FIELD = json_data[JSON_TOP_NODE_DAO_TEMPLATE]['insert_field']
DAO_FUNCTION_INSERT_VALUE = json_data[JSON_TOP_NODE_DAO_TEMPLATE]['insert_value']
DAO_FUNCTION_UPDATE = json_data[JSON_TOP_NODE_DAO_TEMPLATE]['update_field']
DAO_FUNCTION_FILL = json_data[JSON_TOP_NODE_DAO_TEMPLATE]['fill_template']
DAO_FUNCTION_SAVE = json_data[JSON_TOP_NODE_DAO_TEMPLATE]['save_template']
DAO_FUNCTION_SETUP = json_data[JSON_TOP_NODE_DAO_TEMPLATE]['setup_template']

# dynamic module marked block name
DYNAMIC_BLOCK_PROPERTIES_PRIVATE = json_data[JSON_TOP_NODE_DYNAMIC_BLOCK]['PropertiesPrivate']
DYNAMIC_BLOCK_PROPERTIES_ACCESS = json_data[JSON_TOP_NODE_DYNAMIC_BLOCK]['PropertiesAccess']
DYNAMIC_BLOCK_DAO_PUBLIC_CONST = json_data[JSON_TOP_NODE_DYNAMIC_BLOCK]['DAOPublicConst']
DYNAMIC_BLOCK_DAO_INSERT_FIELD = json_data[JSON_TOP_NODE_DYNAMIC_BLOCK]['DAOInsertField']
DYNAMIC_BLOCK_DAO_INSERT_VALUE = json_data[JSON_TOP_NODE_DYNAMIC_BLOCK]['DAOInsertValue']
DYNAMIC_BLOCK_DAO_UPDATE = json_data[JSON_TOP_NODE_DYNAMIC_BLOCK]['DAOUpdate']
DYNAMIC_BLOCK_DAO_FILL = json_data[JSON_TOP_NODE_DYNAMIC_BLOCK]['DAOFill']
DYNAMIC_BLOCK_DAO_SAVE = json_data[JSON_TOP_NODE_DYNAMIC_BLOCK]['DAOSave']
DYNAMIC_BLOCK_DAO_SETUP = json_data[JSON_TOP_NODE_DYNAMIC_BLOCK]['DAOSetup']

# form type
FORM_TYPE_PIT_QUARTER = ''
FORM_TYPE_PIT_MONTH = ''
FORM_TYPE_PIT_YEAR = ''
FORM_TYPE_PIT_SEMI_MONTH = ''
FORM_TYPE_UI_QUARTER = ''
FORM_TYPE_UI_YEAR = ''
FORM_TYPE_VOUCHER = ''

# tax properties
TAX_PROPERTIES_TOTAL_WAGE = 'TotalWage'
TAX_PROPERTIES_TAX_WITHHELD = 'TaxWithheld'
TAX_PROPERTIES_REMITTED = 'Remitted'
TAX_PROPERTIES_UI_TAX_RATE = 'UITaxRate'