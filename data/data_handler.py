import pandas as pd
import chardet

encoding = None

class HandleCSV:

    names = ["YearOfDeath", "DateOfDeath", "GenderDescription", "AgeUnit", "Age",
             "ResidenceCommuneCode", "ResidenceCommuneDescription", "ResidenceRegionDescription",
             "CauseOfDeath",
             "ICD10ChapterCode1", "ICD10ChapterDescription1",
             "ICD10GroupCode1", "ICD10GroupDescription1",
             "ICD10CategoryCode1", "ICD10CategoryDescription1",
             "ICD10SubcategoryCode1", "ICD10SubcategoryDescription1",
             "ExternalCauseOfDeath",
             "ICD10ChapterCode2", "ICD10ChapterDescription2",
             "ICD10GroupCode2", "ICD10GroupDescription2",
             "ICD10CategoryCode2", "ICD10CategoryDescription2",
             "ICD10SubcategoryCode2", "ICD10SubcategoryDescription2",
             "PlaceOfDeath"]

    def __init__(self, path: str):
        self.path = path

    def get_encoding(self) -> str:
        """Gets the encoding of the csv file
        
        Returns:
            str: The encoding of the csv file
        """
        with open(self.path, 'rb') as f:
            result = chardet.detect(f.read())
        return result['encoding']

    def get_dataframe(self, encoding: str) -> pd.DataFrame:
        """Reads the csv file and returns it as a DataFrame
        
        Returns:
            pd.DataFrame: The csv file as a DataFrame
        """
        return pd.read_csv(self.path, encoding=encoding, on_bad_lines='skip', engine='python', sep=';', names=self.names)
