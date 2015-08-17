from app.db import db


class Identity(db.Model):
    __tablename__ = 'identity'

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self):
        pass

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get(_id):
        return Identity.query.filter_by(id=_id).first()
