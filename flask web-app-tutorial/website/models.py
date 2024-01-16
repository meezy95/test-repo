from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

#A database model is just a layout/blueprint for an object that is going to be stored in your dtaabase
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #by default, when you add a new object, you do not need to defnie its ID. The database software is smart enough to increment the IDs,
    #so that they are always unique, so the next ID will just be ID+1 of the last ID that was inserted in the database, and so on.
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class User(db.Model, UserMixin):
     #Whenever you create an object in a database, you need a primary key. A way to uniquely identify the object. Typically an integer
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) #No user can have the same email as another user
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
