from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def home():
    dojos = Dojo.show_all_dojos()
    return render_template('dojos.html', all_dojos=dojos)

@app.route('/new_dojo', methods=['POST'])
def add_dojo():
    Dojo.insert_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def get_one_dojo(dojo_id):
    id = {
        'id': dojo_id
    }
    one_dojo = Dojo.show_dojo_ninjas(id)
    if one_dojo.ninjas[0].id != None:
        ninja_count = len(one_dojo.ninjas)
    else:
        ninja_count = 0
    session['dojo_id'] = dojo_id
    return render_template('ninjas.html', dojo=one_dojo, headcount=ninja_count)

