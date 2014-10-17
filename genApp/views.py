__author__ = 'yansong'

from genApp import app
from flask import render_template
import genApp.genlib.formModules.statePIT as Pit


@app.route('/')
@app.route('/index')
def start():
    user = {'nickname': 'Song',
            'testOther': 'test second',
            'testNone': None}
    for item in user.items():
        print(item[0])
    obj = Pit.GeneratePIT({'a': 'a word',
                           'b': None,
                           'formName': 'FCA941',
                           'd': [1, 2, 3, 4]})
    # obj.write_regular()
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