from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/new_ninja')
def show_new_ninja_form():
    all_dojos = Dojo.show_all_dojos()
    return render_template('new_ninja.html', dojos=all_dojos)

@app.route('/add_ninja', methods=['POST'])
def new_ninja():
    Ninja.insert_ninja(request.form)
    return redirect('/dojos')

@app.route('/ninjas/delete/<int:ninja_id>')
def delete_selected_ninja(ninja_id):
    id = {
        'id': ninja_id
    }
    Ninja.delete_ninja(id)
    return redirect('/dojos/'+ str(session['dojo_id']))

@app.route('/ninjas/edit/<int:ninja_id>')
def edit_page(ninja_id):
    id = {
        'id': ninja_id
    }
    one_ninja = Ninja.show_one_ninja(id)
    all_dojos = Dojo.show_all_dojos()
    return render_template('edit_ninja.html', ninja=one_ninja, dojos=all_dojos)

@app.route('/ninjas/edit', methods=['POST'])
def update_ninja():
    Ninja.update_one_ninja(request.form)
    return redirect('/dojos/'+ str(session["dojo_id"]))
