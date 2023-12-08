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

# Update Users Controller



# Delete Users Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')                                   The variable must be in the path within angle brackets
# def index(id):                                            It must also be passed into the function as an argument/parameter
#     user_info = user.User.get_user_by_id(id)              The it will be able to be used within the function for that route
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.

# Render template is a function that takes in a template name in the form of a string, then any number of named arguments containing data to pass to that template where it will be integrated via the use of jinja
# Redirect redirects from one route to another, this should always be done following a form submission. Don't render on a form submission.