
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models.ninja import Ninja
from flask_app.models import ninja
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Dojo:
    db = "dojos_and_ninjas_schema" 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    # Create Users Models
    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (name)
                VALUES (%(name)s);"""
        result = connectToMySQL(cls.db).query_db(query,data)
        return result
    # Read Users Models
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances
        dojos = []
        # Iterate over the db results and create instances with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas(cls, id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, {"id":id} )
        # results will be a list with things attached to each row. 
        dojo = cls(results[0])
        for row_from_db in results:
            # parse the data to make instances and add them the list.
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "dojo_id": row_from_db["id"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja( ninja_data))
        # print(dojo)
        return dojo


    # Update Users Models



    # Delete Users Models