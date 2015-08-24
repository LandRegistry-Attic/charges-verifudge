import os


DEBUG = True

SQLALCHEMY_DATABASE_URI = os.getenv('VERIFUDGE_DATABASE_URI',
                                    'postgres:///verifudge')
