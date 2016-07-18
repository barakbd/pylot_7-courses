"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class CourseModel(Model):
    def __init__(self):
        super(CourseModel, self).__init__()

    def get_courses(self):
        return self.db.query_db('SELECT * FROM courses ORDER BY created_at DESC')

    def add_course(self, form_details):
        data_new_course =  {
                            'name': form_details['name'],
                            'description': form_details['description']
                            }
        query_course_added = 'INSERT INTO courses (name, description, created_at) VALUES (:name, :description, NOW())'
        return self.db.query_db(query_course_added, data_new_course)

    def select_one_course(self, id):
        print 'select_one_course Model'
        data_id = {'id' :id}
        query_id = 'SELECT * FROM courses WHERE course_id= :id'
        return self.db.query_db(query_id, data_id)

    def delete_course_confirm(self, id):
        data_id = {'id': id }
        query_delete_course = 'DELETE FROM courses WHERE course_id = :id'
        return self.db.query_db(query_delete_course, data_id)


    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True

    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
