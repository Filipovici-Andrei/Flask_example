import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I_guess_it\'s_a password'
