class DbConfig(object):
    USERNAME='root'
    PASSWORD='123456'
    HOST='127.0.0.1'
    PORT='3306'
    DATABASE='py_db1'
    DB_URI='mysql+pymysql://root:123456@127.0.0.1:3306/py_db1?charset=utf8'
    SQLALCHEMY_DATABASE_URI=DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True