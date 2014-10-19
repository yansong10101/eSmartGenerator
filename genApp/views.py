__author__ = 'yansong'

from genApp import app
from flask import render_template
import genApp.genlib.formModules.statePIT as Pit
from string import Template


@app.route('/')
@app.route('/index')
def start():
    user = {'nickname': 'generating code',
            'testOther': 'test second',
            'testNone': None}
    print(Template('${nickname} is ${testOther} project').substitute(user))
    obj = Pit.GeneratePIT({'formName': 'FCA941',
                           'attributes': {
                               'StateTaxWithheld': 'double',
                               'NumForms': 'int',
                               'TotalDue': 'double',
                               'NameControl': 'string'
                           }})
    # obj.write_regular()
    # obj.write_method()
    obj.write_properties()
    # obj.write_dao()
    obj.write_dao_method()

    return render_template('index.html',
                           title='home',
                           user=user)


@app.route('/pit-quarter')
def index():
    form = {'formName': 'CA941',
            'formValue': 10,
            'isValue': True}
    return render_template('main/statePITQ.html',
                           title='home',
                           form=form)
