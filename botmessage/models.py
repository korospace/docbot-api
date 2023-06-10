"""Data models."""
import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from server import db

class BotMessages(db.Model):
    __tablename__ = "log_botmessages"
    id        = db.Column(db.BigInteger,  primary_key=True)
    userId    = db.Column(db.Integer,     nullable=False)
    question  = db.Column(db.String(500), nullable=False)
    answer    = db.Column(db.String(64),  nullable=False)
    created   = db.Column(db.DateTime,    default=datetime.datetime.utcnow, nullable=True)

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.userId     = kwargs.get("userId")
        self.question   = kwargs.get("question")
        self.answer     = kwargs.get("answer")
        self.created    = kwargs.get("created")

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<User {}>".format(self.username)