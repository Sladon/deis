from sqlalchemy import Column, String, Integer
from db.database import Base

class CauseOfDeath(Base):
    __tablename__ = 'cause_of_death'

    id = Column(Integer, primary_key=True)
    description = Column(String, "CauseOfDeath")
    icd10_chapter_code = Column(String, "ICD10ChapterCode1")
    icd10_chapter_description = Column(String, name="ICD10ChapterDescription1")
    icd10_group_code = Column(String, name="ICD10GroupCode1")
    icd10_group_description = Column(String, name="ICD10GroupDescription1")
    icd10_category_code = Column(String, name="ICD10CategoryCode1")
    icd10_category_description = Column(String, name="ICD10CategoryDescription1")
    icd10_subcategory_code = Column(String, name="ICD10SubcategoryCode1")
    icd10_subcategory_description = Column(String, name="ICD10SubcategoryDescription1")