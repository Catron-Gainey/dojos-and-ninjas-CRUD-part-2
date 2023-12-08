from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Ninja:
    db = "dojos_and_ninjas_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?

    @classmethod
    def get_one_ninja(cls, id):
        query = "SELECT * from ninjas WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, {"id":id})
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id)
                VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"""
        result = connectToMySQL(cls.db).query_db(query,data)
        return result
    
    @classmethod
    def delete_ninja(cls, id):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {"id": id}
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update_ninja(cls,user_data):
        query = """UPDATE ninjas 
                SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s
                WHERE id = %(id)s
                ;"""
        return connectToMySQL(cls.db).query_db(query,user_data)