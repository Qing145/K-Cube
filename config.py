import os 

#basedir = os.path.abspath(".")
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    BOOTSTRAP_SERVE_LOCAL= True
    SECRET_KEY="Hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = "Flasky Admin <2500177651@qq.com>"
    FLASKY_ADMIN = "xx@xx.com" # FLASKY_ADMIN

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = '2500177651@qq.com'
    MAIL_PASSWORD = 'wdrhbhhmcumrdhjj'
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"data-dev.sqlite")
    FLASKY_POSTS_PER_PAGE = os.environ.get("FLASKY_POSTS_PER_PAGE") or 8
    FLASKY_FOLLOWERS_PER_PAGE =  os.environ.get("FLASKY_FOLLOWERS_PER_PAGE") or 8
    UPLOADED_PHOTOS_DEST = os.path.join(basedir,"app/uploads")

class TestingConfig(Config):
    TESTING = True    
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"data-test.sqlite")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"data.sqlite")

config = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "productin":ProductionConfig,
    "default":DevelopmentConfig
}