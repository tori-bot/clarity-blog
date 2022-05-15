from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    #model to create new users
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),unique=True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_url=db.Column(db.String())
    comments=db.relationship('Comment',backref='user' ,lazy="dynamic")
    pitches=db.relationship('Pitch',backref='user' ,lazy="dynamic")
    upvotes = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'user', lazy = 'dynamic')
