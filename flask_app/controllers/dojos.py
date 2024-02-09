from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

# Create Users Controller
@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    user_id= Dojo.save(request.form)
    return redirect('/dojos')

# Read Users Controller
# @app.route('/dojos')
# def index():
#     return render_template('dojos.html')
@app.route('/dojos')
def read_all_dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", all_dojos = all_dojos)

@app.route('/dojo/<int:dojo_id>')
def show_dojo_with_ninjas(dojo_id):
    session['dojo_id'] = dojo_id
    dojo = Dojo.get_dojo_with_ninjas(dojo_id)
    return render_template("show_one_dojo.html", dojo = dojo)


# @app.route('/ninjas')
# def new_ninja_page():
#     return render_template("ninjas.html")

