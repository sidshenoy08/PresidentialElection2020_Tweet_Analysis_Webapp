from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from flask import current_app, g

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Ensure tables are created

# def get_db():
#     if 'db_conn' not in g:
#         engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
#         g.db_conn = engine.connect()
#     return g.db_conn

# def close_db(e=None):
#     db_conn = g.pop('db_conn', None)
#     if db_conn is not None:
#         db_conn.close()
