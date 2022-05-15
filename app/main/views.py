from urllib import request
from django.shortcuts import render
from flask import render_template,redirect,url_for,abort
from . import main
from ..  import db,photos
from flask_login import current_user,login_required
from ..models import User,Author,Blog
from .forms import UpdateAdminProfile,UpdateProfile

@main.route('/')
def welcome():
    title='Welcome'
    return render_template('welcome.html',title=title)

@main.route('/author/<uname>')
def adminprofile(uname):
    author=Author.query.filter_by(username=uname).first()
    
    if author is None:
        abort(404)

    return render_template('/profile/admin_profile.html',author=author)

@main.route('/user/<uname>/update',methods=['GET','POST'])
def update_admin_profile(uname):
    author=Author.query.filter_by(username=uname).first()

    if author is None:
        abort(404)
    
    author_update_form=UpdateAdminProfile()

    if author_update_form.validate_on_submit():
        author.bio=author_update_form.bio.data

        db.session.add(author)
        db.session.commit()

        return redirect(url_for('.adminprofile',uname=author.username))
    return render_template('profile/admin_update.html',author_update_form=author_update_form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_admin_pic(uname):
    author= Author.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        author.profile_pic_url = path
        db.session.commit()

    return redirect(url_for('main.adminprofile',uname=uname))
  

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)

    return render_template('/profile/profile.html',user=user)

@main.route('/user/<uname>/update',methods=['GET','POST'])
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    
    form=UpdateProfile()

    if form.validate_on_submit():
        user.bio=form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form=form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user= User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_url = path
        db.session.commit()

    return redirect(url_for('main.profile',uname=uname))