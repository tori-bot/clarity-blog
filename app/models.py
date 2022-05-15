
from email.policy import default
from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from datetime import datetime

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
    
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username} '

class Author(UserMixin,db.Model):
    __tablename__ = 'author'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255 ))
    email=db.Column(db.String(255))
    author_pass=db.Column(db.String(255))
    title=db.Column(db.String(255)
    )
    blog=db.relationship('Blog',backref='author',lazy='dynamic')

    def save_author(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return(f'{self.username } ' )

class Blog(db.Model):
    __tablename__ = 'blog'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    category=db.Column(db.String(255))
    author=db.Column(db.String(255))
    content=db.Column(db.Text())
    published=db.Column(db.DateTime,default=datetime.datetime.utcnow)
    author_id=db.Column(db.Integer(),db.ForeignKey('author.id'))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls, category):
        blogs=Blog.query.filter_by(category=category).all()
        return blogs

    def __repr__(self):
        return(f"{self.author}'s Blogs" )