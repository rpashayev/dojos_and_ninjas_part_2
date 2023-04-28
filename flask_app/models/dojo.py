from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.ninjas = []
    
    @classmethod
    def show_all_dojos(cls):
        all_dojos = []
        query = '''
            SELECT *
            FROM dojos;
        '''
        result = connectToMySQL(cls.DB).query_db(query)
        for dojo in result:
            all_dojos.append(cls(dojo))
        return all_dojos
        
    @classmethod
    def show_one_dojo(cls, data):
        query = '''
                SELECT *
                FROM dojos
                WHERE id= %(id)s;
        '''
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def show_dojo_ninjas(cls, data):
        query = '''
                SELECT *
                FROM dojos
                LEFT JOIN ninjas ON ninjas.dojo_id=dojos.id
                WHERE dojos.id= %(id)s;
        '''
        result = connectToMySQL(cls.DB).query_db(query, data)
        dojo = cls(result[0])

        for row in result:
            ninja_info = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
            }
            dojo.ninjas.append(Ninja(ninja_info))
        return dojo
    
    @classmethod
    def insert_dojo(cls, data):
        query = '''
                INSERT INTO dojos(name)
                VALUES ( %(name)s );
        '''
        return connectToMySQL(cls.DB).query_db(query, data)

