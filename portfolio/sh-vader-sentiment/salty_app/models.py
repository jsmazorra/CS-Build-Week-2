# salty_app/models.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiating the DataBase from the SQLAlchemy Class
db = SQLAlchemy()

# Instantiating Migrate
migrate = Migrate()


# Defining new class "Tweets": inherents db.model from SQLAlchemy above
class Comments(db.Model):
    # Configuring the attributes, and subsequent DB columns
    comment_id = db.Column(db.BigInteger, primary_key=True)
    author_name = db.Column(db.String)
    comment_text = db.Column(db.String)
    salty_comment_score_pos = db.Column(db.Float)
    salty_comment_score_neg = db.Column(db.Float)
