# https://pythonbasics.org/flask-sqlalchemy/

# Need the usual spate of imports here - we can copy them from previous examples
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

# Code the instantiation of the flask app 

# Here, we set up sqlalchemy

# Name our DB first
# General form for sqlalchemy is 'dialect://user:password@server:port/database'
# 'dialect' is an identifier that identifies the database type (sqlite3, in this case)
# sqlite3 does not require use, password, server or port, so we are left with the name (students.sqlite3, here)
# the THREE SLASHES means the path is relative (four is absolute). Remove user:... leaves 3 slashes
# SQLAlchemy stores the db in a folder 'instance' under the app root
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'    
app.config['SECRET_KEY'] = "random string"                              # Required for sqlalchemy (and sessions, etc.)
# We need to create a database object that we use
# to call SQLAlchemy methods to create the db and
# issue CRUD calls against it
db = SQLAlchemy(app)
# This code creates a table in the students DB
# Subclass db.Model, provide table particulars, code __init__ used when creating the table
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)  # identify an ID column
    name = db.Column(db.String(100))                              # These are other columns
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200)) 
    pin = db.Column(db.String(10))
    # aColumn = db.Column(db.String(length=12), nullable=False, unique=True) - additional args to define column

    # __init__ called by SQLAlchemy when creating new rows
    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
        
# Define a function that will execute when the route '/'
# is entered. We need a flask decorator and a method
# This method will display the 'show_all.html' page we previously saw
@app.route('/')
def show_all():
    # Inside the method, we create the DB as shown:
    db.create_all()
    # The 'show_all.html' page shows all students entered
    # Can't show them unless we retrieve them first
    # This line retrieves all the students currently stored in the students db
    all_students = students.query.all()
    # Now, code the flask statement that returns the display (render) of 'show_all.html' page
    # and assigns all_students to the variable in the html page so the 
    # Jinja snippet ' {% for student in students %} renders properly
    return render_template('show_all.html', students = all_students )
    
    
# Define a function that will execute when the route '/new'
# is entered. We need a flask decorator and a method
# The method needs to execute when either a GET HTTP method is issued 
# from the 'show_all.html' page or a POST HTTP method is issued from the
# 'new.html' page
@app.route('/new', methods = ['GET', 'POST'])
def new():  


    # This method will perform separate processing for a POST request and
    # a GET request  
    # IOW, a POST method from 'new.html' ADDS A NEW STUDENT and redirects to
    # the 'show_all.html' page; a GET method from 'show_all.html' allows user
    # to ENTER NEW STUDENT INFO by showing the 'new.html' page
    #
    # Determine if this function was triggered by a POST call and do the following if so:
    # Check if ALL fields were entered. If ANY were not entered, execute the 'flash' flask function
    # if <function triggered by POST>
    #   <check if all fields from the 'new.html' page were entered.
    if request.method == 'POST':
             
        if not request.form['name'] or \
            not request.form['city'] or \
            not request.form['addr'] or \
            not request.form['pin']   :
            flash('Please enter all the fields', 'error')
        else:
            # If all fields were entered (that's how we got to the 'else'),
            # CALL THE CTOR of the 'students' class and pass the entries
            # made in 'new.html', accessible from the 'request' object
            student = students(request.form['name'], request.form['city'],
                                request.form['addr'], request.form['pin'])
            # Add new student to DB, COMMIT THE CHANGE, flash 'successful'
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            # Done with new student processing
            # Show the page 'show_all.html' - this page will include the new student
            return redirect(url_for('show_all'))
    # If we get here, a GET method was sent. We noted that this
    # function is triggered by a GET from the 'show_all.html' page and
    # is a request from the user to display the page that allows us to 
    # enter data for a new student
    # So, show 'new.html' here
    # BTW, no need for 'else' since the 'if' block
    # has a 'return'
    return render_template('new.html')  # When method="GET"

    
# Code boilerplate to run a flask app here
if __name__ == '__main__':
    # The line below was in teh original (from the URL on line 1)
    # This causes an "out of context" error
    # The line was moved in the '/' route method - that's
    # # when we have a flask app (and the correct context)
    # db.create_all()   
    app.run(debug = True)
         
         
