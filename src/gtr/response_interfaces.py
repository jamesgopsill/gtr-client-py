from typing import TypedDict, List, Any
from typing_extensions import NotRequired
from datetime import date


class Response(TypedDict):
    size: int
    total_pages: int
    total_size: int
    page: int


class Link(TypedDict):
    href: str
    rel: str
    start: NotRequired[date]
    end: NotRequired[date]
    other_attributes: Any


class Links(TypedDict):
    link: List[Link]


class Identifier(TypedDict):
    value: str
    type: str


class Identifiers(TypedDict):
    identifiers: List[Identifier]


class HealthCategory(TypedDict):
    id: str
    text: str


class HealthCategories(TypedDict):
    health_category: List[HealthCategory]


class ResearchSubject(TypedDict):
    id: str
    text: str
    percentage: int


class ResearchSubjects(TypedDict):
    researcSubject: List[ResearchSubject]


class ResearchTopic(TypedDict):
    id: str
    text: str


class ResearchTopics(TypedDict):
    research_topics: List[ResearchTopic]


class Participant(TypedDict):
    grant_offer: float
    organisation_id: str
    organisation_name: str
    project_cost: float
    role: str


class ParticipantValues(TypedDict):
    participant: List[Participant]


class Address(TypedDict):
    city: str
    created: date
    id: str
    line1: str
    post_code: str
    region: str
    type: str


class Addresses(TypedDict):
    address: List[Address]


class Person(TypedDict):
    links: Links
    id: str
    href: str
    created: str
    first_name: str
    other_names: str
    surname: str
    orcid_id: NotRequired[str]


class Project(TypedDict):
    links: Links
    id: str
    href: str
    created: date
    identifiers: Identifiers
    title: str
    status: str
    grant_category: str
    lead_funder: str
    lead_organisation_department: NotRequired[str]
    abstract_text: str
    health_categories: HealthCategories
    research_activities: Any
    research_subjects: ResearchSubjects
    research_topics: ResearchTopics
    rcuk_programmes: Any
    participant_values: NotRequired[ParticipantValues]


class Organisation(TypedDict):
    links: Links
    addresses: Addresses
    href: str
    id: str
    name: str


########


class PeopleResponse(Response):
    person: List[Person]


class ProjectsResponse(Response):
    project: List[Project]


class ProjectsOrganisationsResponse(Response):
    organisation: List[Organisation]
