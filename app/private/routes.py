import requests
from flask import Flask, redirect, render_template, request, url_for
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from flask_oidc import OpenIDConnect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.urls import url_parse

from .. import oidc
from . import private_bp

@private_bp.route('/private')
@login_required
def hello_me():
    """Example for protected endpoint that extracts private information from the OpenID Connect id_token.
       Uses the accompanied access_token to access a backend service.
    """

    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])

    username = info.get('preferred_username')
    email = info.get('email')
    user_id = info.get('sub')
    greeting = None

    # try:
    #     from oauth2client.client import OAuth2Credentials
    #     access_token = OAuth2Credentials.from_json(oidc.credentials_store[user_id]).access_token
    #     print('access_token=<%s>' % access_token)
    #     headers = {'Authorization': 'Bearer %s' % (access_token)}
    #     # YOLO
    #     greeting = requests.get('http://localhost:8080/greeting', headers=headers).text
    # except:
    #     print("Could not access greeting-service")
    #     greeting = "Hello %s" % username

    return render_template("private/user_info.html", username=username, user_id=user_id, email=email)     

          