from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)

        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        courses = self.models['Course'].get_courses()
        return self.load_view('courses/index.html', courses=courses)

    def add(self):
        print request.form
        course = request.form
        if len(course['name']) < 15:
            flash("Course name must be at least 15 characters")
            return redirect('/')
        self.models['Course'].add_course(course)
        return redirect('/')

    def destroy(self, id):
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('courses/delete.html', course=course[0])

    def delete(self, id):
        self.models['Course'].delete_course(id)
        return redirect('/')

