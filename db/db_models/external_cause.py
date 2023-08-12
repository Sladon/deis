from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from db.database import Base

class ExternalCauseOfDeath(Base):
    __tablename__ = 'external_cause_of_death'

    id = Column(Integer, primary_key=True)
    description = Column(String, name="ExternalCauseOfDeath")
    icd10_chapter_code = Column(String, "ICD10ChapterCode2")
    icd10_chapter_description = Column(String, name="ICD10ChapterDescription2")
    icd10_group_code = Column(String, name="ICD10GroupCode2")
    icd10_group_description = Column(String, name="ICD10GroupDescription2")
    icd10_category_code = Column(String, name="ICD10CategoryCode2")
    icd10_category_description = Column(String, name="ICD10CategoryDescription2")
    icd10_subcategory_code = Column(String, name="ICD10SubcategoryCode2")
    icd10_subcategory_description = Column(String, name="ICD10SubcategoryDescription2")