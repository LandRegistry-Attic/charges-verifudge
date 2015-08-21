from app.db import db


class Identity(db.Model):
    __tablename__ = 'identity'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    middle_names = db.Column(db.String())
    last_name = db.Column(db.String())
    dob = db.Column(db.String())
    address_line1 = db.Column(db.String())
    address_line2 = db.Column(db.String())
    address_line3 = db.Column(db.String())
    address_line4 = db.Column(db.String())
    address_line5 = db.Column(db.String())
    postcode = db.Column(db.String())
    gender = db.Column(db.String())

    def __init__(
        self, first_name=None, middle_names=None, last_name=None,
        dob=None, address_line1=None, address_line2=None,
        address_line3=None, address_line4=None, address_line5=None,
        postcode=None, gender=None
    ):
        self.first_name = first_name
        self.middle_names = middle_names
        self.last_name = last_name
        self.dob = dob
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.address_line3 = address_line3
        self.address_line4 = address_line4
        self.address_line5 = address_line5
        self.postcode = postcode
        self.gender = gender

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get(_id):
        return Identity.query.filter_by(id=_id).first()

    def all():
        return Identity.query.all()

    def __eq__(self, other):
        return [
            self.first_name, self.middle_names, self.last_name,
            self.dob, self.address_line1, self.address_line2,
            self.address_line3, self.address_line4, self.address_line5,
            self.postcode, self.gender
        ] == [
            other.first_name, other.middle_names, other.last_name,
            other.dob, other.address_line1, other.address_line2,
            other.address_line3, other.address_line4,
            other.address_line5, other.postcode, other.gender
        ]
