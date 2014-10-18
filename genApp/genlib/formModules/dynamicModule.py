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


# get data type for dao.method.cs, example: ToDouble, String
def get_method_data_type(data_type):
    return data_type.title()


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
                                         'attribute': attribute,
                                         'datatype': data_type})


# write general function to do template substitution for small block of code
# TO DO -- see if can relace others with unchanged format
def template_substitution(temp, dicts):
    return Template(temp).substitute(dicts)


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


# ================================ for .properties.cs ==========================
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
# ==============================================================================


# ================================ for dao.method.cs ===========================
# generate DAO.method.cs file public const str for database fields
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


# generate dao.method.cs file sql_insert_field function template
def dao_method_sql_insert_field(dicts):
    if dicts is None:
        return
    insert_field_block = []
    for item in dicts.item():
        key = item[0]
        attribute = get_dao_method_data_member(key)
        # TO DO -- specify dictionary index name, better to make static and save into file
        #       -- Write common used template field name, example : 'formName', 'dataType' ...
        insert_field = template_substitution(Constants.DAO_FUNCTION_INSERT_FIELD, {'field_name': attribute})
        insert_field_block.append(insert_field)
    return insert_field_block


# generate dao.method.cs file sql_insert_value function template
def dao_method_sql_insert_value(dicts):
    if dicts is None:
        return
    insert_value_block = []
    for item in dicts.item():
        key = item[0]
        attribute = get_dao_method_data_member(key)
        # TO DO -- specify dictionary index name, better to make static and save into file
        #       -- Write common used template field name, example : 'formName', 'dataType' ...
        insert_value = template_substitution(Constants.DAO_FUNCTION_INSERT_VALUE, {'field_name': attribute})
        insert_value_block.append(insert_value)
    return insert_value_block


# generate dao.method.cs file update_sql function template
def dao_method_sql_update(dicts):
    if dicts is None:
        return
    update_block = []
    for item in dicts.item():
        key = item[0]
        attribute = get_dao_method_data_member(key)
        # TO DO -- specify dictionary index name, better to make static and save into file
        #       -- Write common used template field name, example : 'formName', 'dataType' ...
        update_value = template_substitution(Constants.DAO_FUNCTION_UPDATE, {'field_name': attribute})
        update_block.append(update_value)
    return update_block


# generate dao.method.cs file fill function template
def dao_method_fill(dicts, form_name):
    if dicts is None:
        return
    fill_block = []
    for item in dicts.item():
        key = item[0]
        value = item[1]
        attribute = get_dao_method_data_member(key)
        data_type = get_method_data_type(value)
        # TO DO -- specify dictionary index name, better to make static and save into file
        #       -- Write common used template field name, example : 'formName', 'dataType' ...
        fill_value = template_substitution(Constants.DAO_FUNCTION_FILL, {'field_name': attribute,
                                                                           'formName': form_name,
                                                                           'property': key,
                                                                           'dataType': data_type})
        fill_block.append(fill_value)
    return fill_block


# generate dao.method.cs file save function template
def dao_method_save(dicts, form_name):
    if dicts is None:
        return
    save_block = []
    for item in dicts.item():
        key = item[0]
        value = item[1]
        attribute = get_dao_method_data_member(key)
        data_type = get_method_data_type(value)
        # TO DO -- specify dictionary index name, better to make static and save into file
        #       -- Write common used template field name, example : 'formName', 'dataType' ...
        save_value = template_substitution(Constants.DAO_FUNCTION_SAVE, {'field_name': attribute,
                                                                           'formName': form_name,
                                                                           'property': key,
                                                                           'dataType': data_type})
        save_block.append(save_value)
    return save_block


# generate dao.method.cs file setup function template
def dao_method_setup(dicts):
    if dicts is None:
        return
    setup_block = []
    for item in dicts.item():
        key = item[0]
        attribute = get_dao_method_data_member(key)
        # TO DO -- specify dictionary index name, better to make static and save into file
        #       -- Write common used template field name, example : 'formName', 'dataType' ...
        setup_value = template_substitution(Constants.DAO_FUNCTION_SETUP, {'field_name': attribute})
        setup_block.append(setup_value)
    return setup_block
# ==============================================================================