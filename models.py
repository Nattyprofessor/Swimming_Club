from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()
class Swimmer(Base):
    __tablename__ = 'swimmers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    style = Column(String)
    best_lap = Column(String)

    coaches = relationship("Coach", back_populates="swimmer")

class Coach(Base):
    __tablename__ = 'coaches'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    swimmer_id = Column(Integer, ForeignKey('swimmers.id'))

    swimmer = relationship("Swimmer", back_populates="coaches")
