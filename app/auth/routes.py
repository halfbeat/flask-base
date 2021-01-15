from flask import render_template, redirect, url_for, request
import requests
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import login_manager
from . import auth_bp
from .forms import SignupForm, LoginForm
from .models import User, users, get_user
from .. import oidc

@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('public.index')
        return redirect(next_page)
    return render_template("auth/signup_form.html", form=form)

@auth_bp.route('/custom_callback')
@oidc.custom_callback
def callback(data):    
    print(oidc.get_access_token())    
    user = User(len(users) + 1, oidc.user_getfield('email'), oidc.user_getfield('email'), oidc.get_access_token())
    users.append(user)
    login_user(user)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('public.index')
    return redirect(next_page)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    return oidc.redirect_to_auth_server(None, 'asdasd')

@auth_bp.route('/logout')
def logout():
    logout_user()
    try:
        logout_request = oidc.user_getfield('iss') + "/protocol/openid-connect/logout?id_token_hint=" + oidc.get_access_token()
        requests.get(logout_request)    
        oidc.logout()
    except:
        pass
    return redirect(url_for('public.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))

