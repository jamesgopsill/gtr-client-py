import requests
import re
import math
from datetime import datetime
from typing import Dict

from .query_interfaces import *
from .response_interfaces import *


class GtR2Client:

    __url: str = "https://gtr.ukri.org/gtr/api"
    __debug: bool = False
    __camel_pat = re.compile(r"([A-Z])")

    def __init__(self, debug: bool = False):
        self.__debug = debug
        return

    def hello(self) -> str:
        return "world"

    def __convert_dates(self, v):
        if isinstance(v, int) and v > 0 and int(math.log10(v)) + 1 == 13:
            return datetime.utcfromtimestamp(v / 1000)
        else:
            return v

    def __camel_to_underscore(self, key: str) -> str:
        return self.__camel_pat.sub(lambda x: "_" + x.group(1).lower(), key)

    def __convert_json(self, d: Dict) -> Dict:
        """
        Converts json keys to underscore case and converts dates into date time objects.
        """
        new_d = {}
        for k, v in d.items():
            if isinstance(v, dict):
                new_d[self.__camel_to_underscore(k)] = self.__convert_json(v)
            elif isinstance(v, list):
                new_list = []
                for obj in v:
                    if isinstance(v, dict):
                        new_list.append(self.__convert_json(obj))
                    else:
                        new_list.append(self.__convert_dates(obj))
                new_d[self.__camel_to_underscore(k)] = new_list
            else:
                new_d[self.__camel_to_underscore(k)] = self.__convert_dates(v)
        return new_d

    def __get(self, method: str, params: Dict = {}) -> Dict:
        url = self.__url + method

        if self.__debug:
            print("|- Query:", url)
            print("|- Params:", params)

        request_params = {}

        key_conversions = {
            "query": "q",
            "page": "p",
            "page_size": "s",
            "sort": "so",
            "search_fields": "f",
            "sort_fields": "sf",
        }

        for k, v in key_conversions.items():
            if k in params:
                request_params[v] = params[k]

        if self.__debug:
            print("|- Request Query:", request_params)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/vnd.rcuk.gtr.json-v7",
        }

        r = requests.get(url, headers=headers, params=request_params, timeout=5)

        if r.ok:
            return self.__convert_json(r.json())
        else:
            print("|- ", r.status_code)
            raise Exception("|- Error with request")

    
    def schema(self, item: str):
        url = self.__url +"/"+ item
        headers = {
            "Accept": "application/vnd.rcuk.gtr.xml-v7"
        }
        r = requests.get(url, headers=headers, timeout=5)

        if not r.ok:
            print("|- ", r.status_code)
            raise Exception("|- Error with request")

        return r.text
    
    def people(self, query: PeopleQuery = {}) -> PeopleResponse:
        return self.__get("/persons", query)

    def projects(self, query: ProjectsQuery = {}) -> ProjectsResponse:
        return self.__get("/projects", query)

    def organisations(self, query: OrganisationsQuery = {}) -> OrganisationsResponse:
        return self.__get("/organisations", query)

    def funds(self, query: FundsQuery = {}) -> FundsResponse:
        return self.__get("/funds", query)

    def outcomes(self, query = {}):
        return self.__get("/outcomes", query)

    ####

    def project_organisations(self, id: str) -> OrganisationsResponse:
        return self.__get("/projects/" + id + "/organisations")

    def project_persons(self, id: str) -> PeopleResponse:
        return self.__get("/projects/" + id + "/persons")

    def project_funds(self, id: str) -> FundsResponse:
        return self.__get("/projects/" + id + "/funds")
