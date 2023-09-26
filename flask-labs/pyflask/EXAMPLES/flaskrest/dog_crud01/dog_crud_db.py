import os
from flask import current_app as app

db_name = app.__name__  +  '.db'
print("DB name:", db_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # must be initialized BEFORE Marshmallowf

