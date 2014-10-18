__author__ = 'yansong'

from genApp import app
from flask import render_template
import genApp.genlib.formModules.statePIT as Pit
from string import Template


@app.route('/')
@app.route('/index')
def start():
    user = {'nickname': 'Song',
            'testOther': 'test second',
            'testNone': None}
    print(Template('${nickname} is ${testOther} project').substitute(user))
    obj = Pit.GeneratePIT({'a': 'a word',
                           'b': None,
                           'formName': 'FCA941',
                           'd': [1, 2, 3, 4]})
<<<<<<< HEAD
=======
    # obj.write_regular()
>>>>>>> c8d3d49c3e14c56bf30a485554e879a1fb2daa25
    obj.write_regular()
    obj.write_method()
    obj.write_properties()
    obj.write_dao()
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
