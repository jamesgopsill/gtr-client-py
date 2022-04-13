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
        url = self.__url + "/" + item
        headers = {"Accept": "application/vnd.rcuk.gtr.xml-v7"}
        r = requests.get(url, headers=headers, timeout=5)

        if not r.ok:
            print("|- ", r.status_code)
            raise Exception("|- Error with request")

        return r.text

    ### Get Objects Methods

    def people(self, query: PeopleQuery = {}) -> PeopleResponse:
        return self.__get("/persons", query)

    def projects(self, query: ProjectsQuery = {}) -> ProjectsResponse:
        return self.__get("/projects", query)

    def organisations(self, query: OrganisationsQuery = {}) -> OrganisationsResponse:
        return self.__get("/organisations", query)

    def funds(self, query: FundsQuery = {}) -> FundsResponse:
        return self.__get("/funds", query)

    def outcomes(self, query: OutcomesQuery = {}) -> OutcomesResponse:
        return self.__get("/outcomes", query)

    def keyfindings(self, query: OutcomesQuery = {}) -> KeyFindingsResponse:
        return self.__get("/outcomes/keyfindings", query)

    def impactsummaries(self, query: OutcomesQuery = {}) -> ImpactSummariesResponse:
        return self.__get("/outcomes/impactsummaries", query)

    def publications(self, query: OutcomesQuery = {}) -> PublicationsResponse:
        return self.__get("/outcomes/publications", query)

    def collaborations(self, query: OutcomesQuery = {}) -> CollaborationsResponse:
        return self.__get("/outcomes/collaborations", query)

    def intellectual_properties(
        self, query: OutcomesQuery = {}
    ) -> IntellectualPropertiesResponse:
        return self.__get("/outcomes/intellectualproperties", query)

    def policy_influences(self, query: OutcomesQuery = {}) -> PolicyInfluencesResponse:
        return self.__get("/outcomes/policyinfluences", query)

    def products(self, query: OutcomesQuery = {}) -> ProductsResponse:
        return self.__get("/outcomes/products", query)

    def research_materials(
        self, query: OutcomesQuery = {}
    ) -> ResearchMaterialsResponse:
        return self.__get("/outcomes/research_materials", query)

    def spin_outs(self, query: OutcomesQuery = {}) -> SpinOutResponse:
        return self.__get("/outcomes/spinouts", query)

    def further_fundings(self, query: OutcomesQuery = {}) -> FurtherFundingsResponse:
        return self.__get("/outcomes/furtherfundings", query)

    def disseminations(self, query: OutcomesQuery = {}) -> DisseminationsResponse:
        return self.__get("/outcomes/disseminations", query)

    ### Get Object methods

    def person(self, id: str) -> Person:
        return self.__get("/persons/" + id)

    def project(self, id: str) -> Project:
        return self.__get("/project/" + id)

    def organisation(self, id: str) -> Organisation:
        return self.__get("/organisations/" + id)

    def fund(self, id: str) -> Fund:
        return self.__get("/funds/" + id)

    def key_finding(self, id: str) -> Person:
        return self.__get("/keyfindings/" + id)

    def impact_summary(self, id: str) -> ImpactSummary:
        return self.__get("/impactsummaries/" + id)

    def publication(self, id: str) -> Publication:
        return self.__get("/publication/" + id)

    def collaboration(self, id: str) -> Collaboration:
        return self.__get("/collaboration/" + id)

    def intellectual_propety(self, id: str) -> IntellectualProperty:
        return self.__get("/intellectualproperties/" + id)

    def policy_influence(self, id: str) -> PolicyInfluence:
        return self.__get("/policyinfluences/" + id)

    def product(self, id: str) -> Product:
        return self.__get("/products/" + id)

    def research_material(self, id: str) -> ResearchMaterial:
        return self.__get("/researchmaterials/" + id)

    def spin_out(self, id: str) -> SpinOut:
        return self.__get("/spinouts/" + id)

    def further_funding(self, id: str) -> FurtherFunding:
        return self.__get("/furtherfundings/" + id)

    def dissemination(self, id: str) -> Dissemination:
        return self.__get("/disseminations/" + id)

    ## Get Associated Object Methods

    def person_projects(self, id: str) -> ProjectsResponse:
        return self.__get("/persons/" + id + "/projects")

    def person_organisations(self, id: str) -> OrganisationsResponse:
        return self.__get("/persons/" + id + "/organisations")

    def project_organisations(self, id: str) -> OrganisationsResponse:
        return self.__get("/projects/" + id + "/organisations")

    def project_persons(self, id: str) -> PeopleResponse:
        return self.__get("/projects/" + id + "/persons")

    def project_funds(self, id: str) -> FundsResponse:
        return self.__get("/projects/" + id + "/funds")

    def project_outcomes(self, id: str) -> OutcomesResponse:
        return self.__get("/projects/" + id + "/outcomes")

    def project_key_findings(self, id: str) -> KeyFindingsResponse:
        return self.__get("/projects/" + id + "/outcomes/keyfindings")

    def project_impact_summaries(self, id: str) -> ImpactSummariesResponse:
        return self.__get("/projects/" + id + "/outcomes/impactsummaries")

    def project_publications(self, id: str) -> PublicationsResponse:
        return self.__get("/projects/" + id + "/outcomes/publications")

    def project_collaborations(self, id: str) -> CollaborationsResponse:
        return self.__get("/projects/" + id + "/outcomes/collaborations")

    def project_intellectual_properties(
        self, id: str
    ) -> IntellectualPropertiesResponse:
        return self.__get("/projects/" + id + "/outcomes/intellectualproperties")

    def project_products(self, id: str) -> ProductsResponse:
        return self.__get("/projects/" + id + "/outcomes/products")

    def project_research_materials(self, id: str) -> ResearchMaterialsResponse:
        return self.__get("/projects/" + id + "/outcomes/researchmaterials")

    def project_spin_outs(self, id: str) -> SpinOutResponse:
        return self.__get("/projects/" + id + "/outcomes/spinouts")

    def project_disseminations(self, id: str) -> DisseminationsResponse:
        return self.__get("/projects/" + id + "/outcomes/disseminations")
