from zipfile import ZipFile
from io import BytesIO
import requests
from os import listdir, makedirs, path
from global_params.paths import PATHS

class WebFile:

    def __init__(self, name: str, source: str, filetype: str):
        self.name = name
        self.source = source
        self.filetype = filetype

    def __check_filename(self, filename: str, dir: str) -> bool:
        """This function checks the existence of a file in the given directory
        
        Args:
            filename (str): The name of the file
            dir (str): The directory where the file should be
        
        Returns:
            Boolean: True if the given filename is in the given directory else False
        """
        csvs = [f for f in listdir(dir) if path.isfile(path.join(dir, f))]
        if filename in csvs: return True
        return False
    
    
    def __check_and_create_directories(self):
        """Verify if paths for the data exists, if not create thems"""
        if not PATHS["results"].exists():
            makedirs(PATHS["results"])
            print("Created directory: %s" % PATHS["results"])
        if not PATHS["dictionaries"].exists():
            makedirs(PATHS["dictionaries"])
            print("Created directory: %s" % PATHS["dictionaries"])
        if not PATHS["csvs"].exists():
            makedirs(PATHS["csvs"])
            print("Created directory: %s" % PATHS["csvs"])

    def __download_zip(self) -> ZipFile:
        """Downloads the zip file
        
        Returns:
            ZipFile: ZipFile object"""

        request = requests.get(self.source)
        zip_file = ZipFile(BytesIO(request.content))
        return zip_file
    
    def __extract_zip(self) -> None:
        """Extracts the zip file"""
        self.__check_and_create_directories()

        print("Downloading file from: %s" % self.source)
        file = self.__download_zip()
        print("Finished downloading file")
        
        for i in range(len(file.filelist)):
            filename = file.filelist[i].filename
            print("Extracting file: %s" % filename)
            if 'DEFUNCIONES' in filename: 
                if not self.__check_filename(filename, PATHS["csvs"]): file.extract(filename, PATHS["csvs"])
            elif 'Diccionario' in filename:
                if not self.__check_filename(filename, PATHS["dictionaries"]): file.extract(filename, PATHS["dictionaries"])

    
    def extract(self) -> None:
        """Downloads and extracts the file"""
        if self.filetype == 'zip':
            self.__extract_zip()