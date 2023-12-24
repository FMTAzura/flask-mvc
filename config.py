import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://apisia_wordmemory:38a7fb059d0473aaaea1f4e62efe8d0ac85d31bf@l49.h.filess.io:3307/apisia_wordmemory'

SQLALCHEMY_TRACK_MODIFICATIONS = False