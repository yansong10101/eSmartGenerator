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
            'string': 'string.Empty',
            'DateTime': 'DateTime.MinValue',
            'bool': 'false',
            'DataRow': 'null',
            'DataTable': 'null',
            'DataSet': 'null'}[data_type]


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
                    hasChanged = true;
                }
            }
        }
        '''
    return Template(template).substitute({'name': name,
                               'attributes': attribute,
                               'datatype': data_type})


# return private data member, example: 'm_d_DataMember'
def get_properties_data_member(name, data_type):
    return Constants.VAR_PREFIX_DATA_MEMBER + get_type_char(data_type) + name


def get_dao_method_data_member(name):
    return Constants.VAR_DAO_PREFIX_FIELD + name.upper()


# format string by passed in parameters
def get_att_combination(privilege, data_type, attribute, init_val, is_const):
    const_str = ''
    if is_const:
        const_str = 'const '
        data_type = 'string'
    return '{0} {1}{2} {3} = {4};'.format(privilege, const_str, data_type,
                                          attribute, init_val)


def get_database_field(name):
    return '"{0}"'.format(name)


# generate code for '.properties.cs' private initial module
# return a list of initial lines
def properties_private_module(dicts):
    if dicts is None:
        return
    private_block = []
    # loop dictionary and generate codes
    # item[0] key is attribute name, exactly use in the code
    # item[1] value is the data type of this attribute
    for item in dicts.items():
        key = item[0]
        value = item[1]
        attribute = get_properties_data_member(key, value)
        init_val = get_type_init(value)
        attribute_temp = get_att_combination(Constants.PRIVILEGE_PRIVATE,
                                             value, attribute, init_val, False)
        private_block.append(attribute_temp)
    return private_block


def properties_accessories_module(dicts):
    if dicts is None:
        return
    access_block = []
    for item in dicts.items():
        key = item[0]
        value = item[1]
        attribute = get_properties_data_member(key, value)
        access_temp = get_access_template(key, attribute, value)
        access_block.append(access_temp)
    return access_block


def dao_method_public(dicts):
    if dicts is None:
        return
    dao_public_block = []
    for item in dicts.items():
        key = item[0]
        value = item[1]
        attribute = get_dao_method_data_member(key)
        init_val = get_database_field(key)
        attribute_temp = get_att_combination(Constants.PRIVILEGE_PUBLIC,
                                             value, attribute, init_val, True)
        dao_public_block.append(attribute_temp)
    return dao_public_block