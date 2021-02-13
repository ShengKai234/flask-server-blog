class BasicConfig:
    TYPE = 'THIS IS BASIC MODE'

class DevConfig(BasicConfig):
    TYPE = 'THIS IS DEV MODE'

class TestConfig(BasicConfig):
    TYPE = 'THIS IS TEST MODE'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://db-user:password@localhost:3306/lovemysqldb'

config = {
    'dev': DevConfig,
    'test': TestConfig
}