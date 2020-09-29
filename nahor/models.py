from . import db

class Shortify(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash_identifier = db.Column(db.String(100))
    original_url = db.Column(db.String(1000))
