import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.modules.constants import Constants
from database import Base


class Organization(Base):
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    status = Column(Integer, default=Constants.ORGANIZATION_STATUS_ACTIVE, nullable=False)
    created = Column(DateTime(), default=datetime.datetime.utcnow())
    modified = Column(DateTime(), default=datetime.datetime.utcnow())

    # def __init__(self, name=None, email=None):
    #     self.name = name
    #     self.email = email

    def __repr__(self):
        return '<Organization %r>' % self.name
