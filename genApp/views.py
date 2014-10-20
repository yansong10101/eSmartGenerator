__author__ = 'yansong'

from genApp import app
from flask import render_template, jsonify, request
import json
import genApp.genlib.formModules.statePIT as Pit
from string import Template


@app.route('/')
@app.route('/index')
def start():
    user = {'nickname': 'generating code',
            'testOther': 'test second',
            'testNone': None}
    # obj = Pit.GeneratePIT({'formName': 'FCA941',
    #                        'attributes': {
    #                            'StateTaxWithheld': 'double',
    #                            'NumForms': 'int',
    #                            'TotalDue': 'double',
    #                            'NameControl': 'string'
    #                        }})
    # obj.write_regular()
    # obj.write_method()
    # obj.write_properties()
    # obj.write_dao()
    # obj.write_dao_method()
    return render_template('index.html',
                           title='home',
                           user=user)


@app.route('/temp_json')
def add_numbers():
    obj = Pit.GeneratePIT({'formName': 'FCA941',
                           'attributes': request.args})
    obj.write_regular()
    obj.write_method()
    obj.write_properties()
    obj.write_dao()
    obj.write_dao_method()
    return render_template('main/statePIT.html')


@app.route('/pit')
def index():
    return render_template('main/statePIT.html')