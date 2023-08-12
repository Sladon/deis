from sqlalchemy import Column, Integer, String
from db.database import Base

class Commune(Base):
    __tablename__ = 'communes'

    code = Column(Integer, name="ResidenceCommuneCode", primary_key=True)
    description = Column(String, name="ResidenceCommuneDescription")
    region = Column(String, name="ResidenceRegionDescription")