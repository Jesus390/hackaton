from app.extensions import db
from flask_login import UserMixin

class Professional(UserMixin, db.Model):
    __tablename__ = 'professionals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    profession = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)
    experience_years = db.Column(db.Integer)
