from flaskblog import db
import json

class poi(db.Model):
    unique_id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(30))
    text = db.Column(db.String(1000))
    country = db.Column(db.String(20))

    def __repr__(self):
        return f"poi('{self.username}','{self.country}','{self.text}','{self.unique_id}')"

