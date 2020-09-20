# coding: utf-8
from app import db


class PersonalCollection(db.Model):
    __tablename__ = 'personal_collection'

    id = db.Column(db.BigInteger, primary_key=True)
    save_path = db.Column(db.Text)


class WorkCollection(db.Model):
    __tablename__ = 'work_collection'

    id = db.Column(db.BigInteger, primary_key=True)
    save_path = db.Column(db.Text)
