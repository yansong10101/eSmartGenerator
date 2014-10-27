__author__ = 'yansong'
import genApp.genlib.CommonConstants as Constants
from string import Template


# get prefix by passed in data type
def get_type_char(data_type):
    return {'double': 'd_',
            'int': 'i_',
            'string': 's_',
            'DateTime': 'dt_',
            'DataTable': 'dt_',
            'bool': 'b',
            'DataRow': 'dr_',
            'DataSet': 'ds_'}[data_type]


# get initial value by passed in data type
def get_type_init(data_type):
    return {'double': '0.00',
            'int': '0',
            'string': 'string.Empty',
            'DateTime': 'DateTime.MinValue',
            'bool': 'false',
            'DataRow': 'null',
            'DataTable': 'null',
            'DataSet': 'null'}[data_type]


# To DB database
def get_method_db_data_type(data_type):
    obj = {'int': 'Int32',
           'DateTime': 'DataTime',
           'bool': 'Boolean'}
    if obj.__contains__(data_type) is True:
        return obj[data_type]
    return data_type.title()


# get data type for dao.method.cs, example: ToDouble, String
def get_method_data_type(data_type):
    return get_method_db_data_type(data_type)


# return setter&&getter template
def get_access_template(name, attribute, data_type):
    template = '''
       [XmlElement("${name}")]
       public ${datatype} ${name}
       {
           get { return ${attribute}; }
           set
           {
               if (${attribute} != value)
               {
                ${attribute} = value;
                    _hasChanged = true;
                }
            }
        }
        '''
    return Template(template).substitute({'name': name, 'attribute': attribute, 'datatype': data_type})


# write general function to do template substitution for small block of code
# TO DO -- see if can replace others with unchanged format
def template_substitution(temp, dicts):
    return Template(temp).substitute(dicts)


# return private data member, example: 'm_d_DataMember'
def get_properties_data_member(name, data_type):
    return Constants.VAR_PREFIX_DATA_MEMBER + get_type_char(data_type) + name


# get dao method const data member, example: 'FIELD_CONST'
def get_dao_method_data_member(name):
    return Constants.VAR_DAO_PREFIX_FIELD + name.upper()


# format string by passed in parameters
def get_att_combination(privilege, data_type, attribute, init_val, is_const):
    const_str = ''
    if is_const:
        const_str = 'const '
        data_type = 'string'
    return '{0} {1}{2} {3} = {4};'.format(privilege, const_str, data_type, attribute, init_val)


def get_database_field(name):
    return '"{0}"'.format(name)


class GenerateModule:

    def __init__(self, dicts, form_name):
        if dicts is None:
            return
        self.dicts = dicts
        self.formName = form_name
        self.private_block = []
        self.access_block = []
        self.dao_public_block = []
        self.insert_field_block = []
        self.insert_value_block = []
        self.update_block = []
        self.fill_block = []
        self.save_block = []
        self.setup_block = []

    def set_modules(self):
        for item in self.dicts.items():
            key = item[0]
            value = item[1]
            # ** properties block **
            properties_attribute = get_properties_data_member(key, value)
            properties_init_val = get_type_init(value)
            attribute_temp = get_att_combination(Constants.PRIVILEGE_PRIVATE, value, properties_attribute,
                                                 properties_init_val, False)
            self.private_block.append(attribute_temp)
            access_temp = get_access_template(key, properties_attribute, value)
            self.access_block.append(access_temp)
            # ** dao method block **
            dao_attribute = get_dao_method_data_member(key)
            if value == 'int':
                value = 'int32'
            dao_init_val = get_database_field(key)
            data_type = get_method_data_type(value)
            replaced_attr = {'field_name': dao_attribute,
                             'formName': self.formName,
                             'property': key,
                             'dataType': data_type}
            self.dao_public_block.append(get_att_combination(Constants.PRIVILEGE_PUBLIC, value, dao_attribute,
                                                             dao_init_val, True))
            self.insert_field_block.append(template_substitution(Constants.DAO_FUNCTION_INSERT_FIELD, replaced_attr))
            self.insert_value_block.append(template_substitution(Constants.DAO_FUNCTION_INSERT_VALUE, replaced_attr))
            self.update_block.append(template_substitution(Constants.DAO_FUNCTION_UPDATE, replaced_attr))
            self.fill_block.append(template_substitution(Constants.DAO_FUNCTION_FILL, replaced_attr))
            self.save_block.append(template_substitution(Constants.DAO_FUNCTION_SAVE, replaced_attr))
            self.setup_block.append(template_substitution(Constants.DAO_FUNCTION_SETUP, replaced_attr))

    def get_properties_private_array(self):
        return self.private_block

    def get_properties_access_array(self):
        return self.access_block

    def get_dao_public_array(self):
        return self.dao_public_block

    def get_dao_insert_field_array(self):
        return self.insert_field_block

    def get_dao_insert_value_array(self):
        return self.insert_value_block

    def get_dao_update_array(self):
        return self.update_block

    def get_dao_fill_array(self):
        return self.fill_block

    def get_dao_save_array(self):
        return self.save_block

    def get_dao_setup_array(self):
        return self.setup_block