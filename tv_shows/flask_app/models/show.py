from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Show:
    db = "tv_shows_schema"
    def __init__(self, data):
        self.id = data['id'] 
        self.title = data['title']
        self.network = data['network']
        self.make = data['make']
        self.release_date = data['release_date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
    
    
    @classmethod
    def get_all_shows(cls):
        query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        shows = []
        for row in results:
            show = cls(row)
            user_data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            show.user = user.User(user_data)
            shows.append(show)
        return shows

    @classmethod
    def save(cls,data):
        query = "INSERT INTO shows (title, network, release_date, description, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls,data):
        query = "UPDATE shows SET title=%(title)s, network=%(network)s, release_date=%(release_date)s, description=%(description)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    
    @classmethod
    def get_by_show_id(cls,data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @staticmethod
    def validate_show(show):
        is_valid = True
        query = "SELECT * FROM shows WHERE title = %(title)s;"
        results = connectToMySQL(Show.db).query_db(query, show)
        if len(show['title']) < 3:
            flash('show title must include at least 3 characters', 'add') #changed to add from create
            is_valid = False
        if len(show['network']) < 3:
            flash('show network must include at least 3 characters', 'add')
            is_valid = False
        if str(show['release_date']) == '' or int(show['release_date']) <= 0:
            flash('show price must be greater than 0', 'create')
            is_valid = False
        if len(show['description']) < 3:
            flash('show description must have at least 8 characters', 'add')
            is_valid = False
        return is_valid