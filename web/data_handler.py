import requests

class WebData:
    """
    Client object that connects to Deis Chile website and extracts data.

    Args:
            url (str): URL of Deis website
    """

    def __init__(self, url: str) -> None:
        self.URL = url
        self.headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-User': '?1',
                        }

    def __get_json(self) -> dict:
        """Gets the json from the class url

        Returns:
            dict: The json from the url
        """
        request = requests.get(self.URL, headers=self.headers)
        print(request)
        print(self.URL, self.headers)
        data = request.json()
        return data
    
    def get_options(self) -> dict:
        """Parse the json and returns a dictionary with only the useful data
            
        Returns:
            dict: The parsed json
        """
        data = self.__get_json()
        new_data = {}
        for i in range(len(data)):
            value = data[i]['value']
            name = value['nombre']
            download_link = value['ver']
            new_data[i] = { 'name': name, 'source': download_link }
        
        return new_data
    
    def get_option_information(self, option:int, data: dict) -> list[str, str, str]:
        """Given an option and the data, this function will return the name, source and file type of the option

        Args:
            option (int): The option to get the information from
            data (dict): The data to get the information from
        
        Returns:
            list[str, str, str]: The name, source and file type of the option
        """
        return [data[option]['name'], data[option]['source'], self.__get_filetype(data[option]['source'])]
        
    
    def __get_filetype(self, url: str) -> str:
        """Given a url, this function will return the file type

        Args:
            url (str): The url to get the file type from

        Returns:
            str: The file type
        """
        return url.split('.')[-1]