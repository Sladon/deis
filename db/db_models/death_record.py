from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class DeathRecord(Base):
    __tablename__ = 'death_records'

    id = Column(Integer, primary_key=True)
    year_of_death = Column(Integer, name="YearOfDeath")
    date_of_death = Column(Date, name="DateOfDeath")
    gender_description = Column(String, name="GenderDescription")
    age_unit = Column(Integer, name="AgeUnit")
    age = Column(Integer, name="Age")
    place_of_death = Column(String, name="PlaceOfDeath")

    commune_code = Column(Integer, ForeignKey('communes.code'))
    commune = relationship('Commune')

    cause_of_death_id = Column(Integer, ForeignKey('cause_of_death.id'))
    cause_of_death = relationship('CauseOfDeath')

    external_cause_of_death_id = Column(Integer, ForeignKey('external_cause_of_death.id'))
    external_cause_of_death = relationship('ExternalCauseOfDeath')