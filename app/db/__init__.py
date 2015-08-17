from app.db.db import db, init


__all__ = [init, db]


class AlembicVersion(db.Model):
    __tablename__ = 'alembic_version'

    version_num = db.Column(db.String(), primary_key=True)
