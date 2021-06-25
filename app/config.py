import secrets


class Config(object):
    SECRET_KEY = str(secrets.token_hex(5))
