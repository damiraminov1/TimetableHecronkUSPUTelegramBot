from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

from config import Config

Base = declarative_base()
engine = create_engine(Config.DATABASE_URL, echo=True)
Base.metadata.bind = engine
session = scoped_session(sessionmaker())(bind=engine)


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False)
    group_id = Column(Integer, ForeignKey("Group.id"))
    group = relationship("Group", back_populates="users")

    def __repr__(self):
        return '<User {}>'.format(self.id)


class Group(Base):
    __tablename__ = 'Group'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=256))
    content = Column(String(length=32768))
    local_update = Column(TIMESTAMP(True), nullable=False)
    users = relationship("User", back_populates="group")

    def __repr__(self):
        return 'Group {}'.format(self.id)
