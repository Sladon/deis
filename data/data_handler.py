import pandas as pd
import chardet
from global_params.paths import PATHS
import os

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

    def __init__(self, path: str, split_cut: int = 3):
        self.path = path
        self.name = self.__get_name(split_cut)

    def __get_name(self, split_cut) -> str:
         filemame = os.path.basename(self.path)
         split_name = filemame.split('_')[split_cut:]
         name = '_'.join(split_name).split(".")[0]
         return name

    def get_encoding(self) -> str:
        """Gets the encoding of the csv file
        
        Returns:
            str: The encoding of the csv file
        """
        with open(self.path, 'rb') as f:
            result = chardet.detect(f.read())
        return result['encoding']

    def get_dataframe(self, encoding: str = "ISO-8859-1") -> pd.DataFrame:
        """Reads the csv file and returns it as a DataFrame
        
        Returns:
            pd.DataFrame: The csv file as a DataFrame
        """
        return pd.read_csv(self.path, encoding=encoding, on_bad_lines='skip', engine='python', sep=';', names=self.names)

    def save_dfs_by_year_to_dir(self, encoding = "ISO-8859-1", output_dir = PATHS['csvs']):
        """Saves the DataFrames to CSV by year files in the specified directory
        
        Args:
            output_dir (str): Directory where CSV files will be saved
        """
        df = self.get_dataframe(encoding)
        
        df['YearOfDeath'] = df['YearOfDeath'].astype(str)
        df['YearOfDeath'] = df['YearOfDeath'].str.extract('(\d+)', expand=False)
        df['YearOfDeath'] = pd.to_numeric(df['YearOfDeath'], errors='coerce')

        unique_years = df['YearOfDeath'].unique()

        df_by_year = {}

        for year in unique_years:
            df_by_year[year] = df[df['YearOfDeath'] == year]

        if not os.path.exists(output_dir):
            print(f"Creating {output_dir}")
            os.makedirs(output_dir)

        save_path = output_dir.joinpath(self.name)

        if not os.path.exists(save_path):
            print(f"Creating {save_path}")
            os.makedirs(save_path)

            for year, df in df_by_year.items():
                output_path = os.path.join(save_path, f'data_{year}.csv')
                df.to_csv(output_path, index=False)
        else:
            print(f"Folder already exists {save_path}, delete it if needed")