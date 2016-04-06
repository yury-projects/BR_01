import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, SmallInteger

from app.modules.constants import Constants
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    org_id = Column(Integer, ForeignKey("organization.id"))
    email = Column(String(120), unique=True)
    password = Column(String(120), nullable=False)
    salt = Column(String(120), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(SmallInteger, default=Constants.USER_ROLE_USER, nullable=False)
    status = Column(SmallInteger, default=Constants.USER_STATUS_ACTIVE, nullable=False)
    created = Column(DateTime(), default=datetime.datetime.utcnow())
    modified = Column(DateTime(), default=datetime.datetime.utcnow())


    # def __init__(self, name=None, email=None):
    #     self.name = name
    #     self.email = email

    def __repr__(self):
        return '<User %r>' % self.email
