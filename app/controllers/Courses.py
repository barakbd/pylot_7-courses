"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('CourseModel')
        self.db = self._app.db

    def index(self):
        courses = self.models['CourseModel'].get_courses()
        print 'course list: ',courses
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('index.html', courses=courses)

    def add_course(self):
        if not request.form['course_name']:
            flash('Course name required', 'alert')
            print 'flash', flash
        else:
            new_course_details = {
                                'name': request.form['course_name'],
                                'description': request.form['description']
                                }
            new_course=self.models['CourseModel'].add_course(new_course_details)
            flash ('course added succesfully', 'success')
            print 'new course is ', new_course
        return redirect('/')

    def show_course(self, id):
        print 'delete_course ControllerMemthod'
        one_course = self.models['CourseModel'].select_one_course(id)
        return self.load_view('confirm_delete.html', one_course=one_course, id=id)

    def delete_course_confirm(self, id):
        print 'delete_course_confirm Controller'
        deleted_course = self.models['CourseModel'].delete_course_confirm(id)
        flash('Course deleted succesfully!', 'success')
        return redirect('/')
