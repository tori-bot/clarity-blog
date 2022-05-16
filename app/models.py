
from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    user=db.relationship('User',backref='roles',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

class User(UserMixin,db.Model):
    #model to create new users
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),unique=True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_url=db.Column(db.String())
    role_id=db.Column(db.Integer, db.ForeignKey('roles.id'))
    comments=db.relationship('Comment',backref='user',lazy='dynamic')
    
    

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
    bio=db.Column(db.String(255))
    profile_url=db.Column(db.String())
    email=db.Column(db.String(255))
    author_pass=db.Column(db.String(255))
    blog=db.relationship('Blog',backref='authors',lazy='dynamic')

    def save_author(self):
        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.author_pass = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.author_pass,password)


    def __repr__(self):
        return(f'{self.username } ' )

class Blog(db.Model):
    __tablename__ = 'blog'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    category=db.Column(db.String(255))
    pename=db.Column(db.String(255))
    content=db.Column(db.Text)
    published=db.Column(db.DateTime,default=datetime.utcnow)
    author_id=db.Column(db.Integer,db.ForeignKey('author.id'))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls, category):
        blogs=Blog.query.filter_by(category=category).all()
        return blogs

    def __repr__(self):
        return(f"{self.pename}'s Blogs" )

class Comment(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    blog_id_comment=db.Column(db.Integer,db.ForeignKey('blog.id',ondelete='CASCADE'))
    content=db.Column(db.Text)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def add_comment(cls,id):
        comment = Comment(user = current_user, blog_id=id)
        comment.save_comment()

    @classmethod
    def get_comment(cls,id):
        comments=Comment.query.filter_by(blog_id=id).all()
        return comments

    def __repr__(self):
        return(f"User('{self.content}', '{self.posted}')")

class Quotes:
    def __init__(self,id,author,quote):
        self.id=id
        self.author=author
        self.quote=quote
