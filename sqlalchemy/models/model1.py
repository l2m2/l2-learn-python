from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.dialects import postgresql
from .base import Base


class Model1(Base):
  __tablename__ = "model1"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  attr_data = Column(postgresql.JSONB)
  tags = Column(postgresql.ARRAY(String, dimensions=1))

  def __repr__(self):
    return f"name: {self.name}"
