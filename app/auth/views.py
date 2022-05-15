from flask import render_template,redirect,url_for,flash,request
from ..models import User,Author
from .forms import LoginForm, RegistrationForm,AuthorLoginForm,AuthorRegisterForm
from flask_login import login_user,logout_user,login_required
from ..email import mail_message
from . import auth
from .. import db

@auth.route('/register',methods=['GET','POST'])
def register():
    title = "New Account"
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message(" Welcome to Clarity Blog.","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html',title=title,registration_form = form)

@auth.route('/login',methods=['GET','POST'])
def login():
    title='Clarity Blog Login'

    login_form=LoginForm()

    if login_form.validate_on_submit():
        user=User.query.filter_by(email=login_form.email.data).first()

        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    return render_template('auth/login.html',title=title,login_form=login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.welcome'))


@auth.route('/adminregister',methods=['GET','POST'])
def adminregister():
    title = "New Account"
    author_register_form = AuthorRegisterForm()
    if author_register_form.validate_on_submit():
        author = Author(email = author_register_form.email.data, username = author_register_form.username.data,password = author_register_form.password.data)
        db.session.add(author)
        db.session.commit()

        mail_message(" Welcome to Clarity Blog.","email/welcome_user",author.email,author=author)

        return redirect(url_for('auth.adminlogin'))
        
    return render_template('auth/admin_register.html',title=title,author_register_form = author_register_form)

@auth.route('/adminlogin',methods=['GET','POST'])
def adminlogin():
    title='Clarity Blog Login'

    author_login_form=AuthorLoginForm()

    if author_login_form.validate_on_submit():
        author=Author.query.filter_by(email=author_login_form.email.data).first()

        if author is not None and author.verify_password(author_login_form.password.data):
            login_user(author,author_login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.adminprofile'))

        flash('Invalid username or Password')

    return render_template('auth/admin_login.html',title=title,author_login_form=author_login_form)




