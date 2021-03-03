from sqlalchemy import Boolean, Column, Integer, String
from .base import Base


class User(Base):
  __tablename__ = "sys_user"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True, nullable=False)
  fullname = Column(String)
  email = Column(String)
  password = Column(String, nullable=False)
  is_active = Column(Boolean(), default=True)
  is_superuser = Column(Boolean(), default=False)

  def __repr__(self):
    return f"<User(username = {self.username}, fullname = {self.fullname})>"
