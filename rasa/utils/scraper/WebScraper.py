import json
import requests
from bs4 import BeautifulSoup
from datetime import date
from typing import Text, Dict

class WebScraper:
    """
    Performs web scraping from a url. 
    Get web title and date of webscraping by default.
    Allows custom webscraping through a json file.
    """

    def __init__(self, url: Text) -> None:
        self.DEFAULT_CONFIG_URI = "utils/scraper/config/options.json"
        self._url = url
        self._all_data = {}
        self._get_soup()
        self._get_conf()
        self._scrap_default_metadata()
        self._scrap_custom_metadata()
        
    def _get_soup(self) -> None:
        try:
            response = requests.get(self._url)
            if response and response.status_code == 200:
                html = response.content
                self._soup = BeautifulSoup(html, 'lxml')
            else:
                raise requests.RequestException("Connection error.\nStatus code: " + response.status_code)
        except:
            raise requests.RequestException("Connection error.")
            
    def _get_conf(self) -> None:
        try:
            file = open(file=self.DEFAULT_CONFIG_URI, mode="r", encoding="UTF8")
            self._conf = json.loads(file.read())
        except:
            raise FileNotFoundError('options.json file not found')
        finally:
            file.close()

    def _scrap_default_metadata(self) -> None:
        try:
            self._all_data["title"] = self._soup.title.string
            self._all_data["date"] = str(date.today())
            self._all_data["url"] = str(self._url)
            self._all_data["area"] = None
            self._all_data["type"] = None
            self._all_data["sector"] = None
        except:
            raise Exception("Could not extract custom metadata.")

    def _scrap_custom_metadata(self) -> None:
        try:
            for simple_data in self._conf["metadata"]:
                ctrl_size = 0
                name = simple_data["name"]
                self._all_data[name] = None
                if "attrs" in simple_data.keys():
                    for attr in simple_data["attrs"]:
                        content = self._soup.find(simple_data["label"], attrs=attr)
                        if content and len(content['content']) > ctrl_size:
                            self._all_data[name] = content['content']
                            self._all_data[name] = content['content'].replace("\n", " ")
                            ctrl_size = len(self._all_data[name])
                if "class_" in simple_data.keys():           
                    for class_ in simple_data["class_"]:
                        content = self._soup.find(simple_data["label"], class_=class_)
                        if content and len(content['content']) > ctrl_size:
                            self._all_data[name] = content['content'].replace("\n", " ")
                            ctrl_size = len(self._all_data[name])
        except:
            raise Exception("Could not extract custom metadata.")
            
    @property
    def get_title(self) -> Text:
        return self._all_data["title"]

    @property
    def get_date(self) -> Text:
        return self._all_data["date"]
    
    @property
    def get_url(self) -> Text:
        return self._all_data["url"]
    
    @property
    def get_area(self) -> Text:
        return self._all_data["area"]
    
    @property
    def get_type(self) -> Text:
        return self._all_data["type"]
    
    @property
    def get_sector(self) -> Text:
        return self._all_data["sector"]
    
    @property
    def get_all_data(self) -> Dict:
        return self._all_data
    
if __name__ == "__main__":
    print(WebScraper("https://www.wired.com/science/").get_all_data)