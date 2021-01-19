# config/default.py

SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
SQLALCHEMY_TRACK_MODIFICATIONS = False

TESTING =  True
DEBUG =  True
OIDC_CLIENT_SECRETS =  'client_secrets.json'
OIDC_ID_TOKEN_COOKIE_SECURE =  False
OIDC_REQUIRE_VERIFIED_EMAIL =  False
OIDC_USER_INFO_ENABLED =  True
OIDC_OPENID_REALM =  'flask-demo'
OIDC_SCOPES =  ['openid', 'email', 'profile']
OIDC_INTROSPECTION_AUTH_METHOD =  'client_secret_post'
OVERWRITE_REDIRECT_URI =  'http://localhost:5000/custom_callback'        
