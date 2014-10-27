__author__ = 'yansong'

from genApp import app
from flask import render_template, request
import genApp.genlib.formModules.statePIT as Pit


@app.route('/')
@app.route('/index')
def start():
    user = {'nickname': 'generating code',
            'testOther': 'test second',
            'testNone': None}
    return render_template('index.html',
                           title='home',
                           user=user)


@app.route('/temp_json')
def add_numbers():
    data = request.args
    form_name = data['formName']
    form_type = data['formType']
    form_att = {}
    for item in data.items():
        key = item[0]
        value = item[1]
        if key != 'formName' and key != 'formType':
            form_att[key] = value
    if form_type == 'PIT':
        obj = Pit.GeneratePIT({'formName': form_name,
                               'attributes': form_att})
        obj.write_all()
    elif form_type == 'UI':
        print('not has UI yet...')
        pass
    return render_template('main/statePIT.html')


@app.route('/pit')
def index():
    return render_template('main/statePIT.html')