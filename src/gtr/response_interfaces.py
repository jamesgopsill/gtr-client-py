from re import S
from time import strftime
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


class ValuePounds(TypedDict):
    currencyCode: str
    amount: float


######


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


class Fund(TypedDict):
    links: Links
    id: str
    href: str
    created: date
    start: NotRequired[date]
    end: NotRequired[date]
    valuePounds: ValuePounds
    category: NotRequired[str]
    created: NotRequired[str]

class KeyFinding(TypedDict):
    description: str
    non_academic_uses: str
    exploitation_pathways: str

class Publication(TypedDict):
    title: str
    type: NotRequired[str]
    abstract_text: NotRequired[str]
    other_information: NotRequired[str]
    journal_title: NotRequired[str]
    date_published: NotRequired[date]
    publication_url: NotRequired[str]
    pub_med_id: NotRequired[str]
    isbn: NotRequired[str]
    issn: NotRequired[str]
    series_number: NotRequired[str]
    series_title: NotRequired[str]
    sub_title: NotRequired[str]
    volume_title: NotRequired[str]
    doi: NotRequired[str]
    volume_number: NotRequired[str]
    issue: NotRequired[str]
    total_pages: NotRequired[str]
    edition: NotRequired[str]
    chapter_number: NotRequired[str]
    chapter_title: NotRequired[str]
    page_reference: NotRequired[str]
    conference_event: NotRequired[str]
    conference_location: NotRequired[str]
    conference_number: NotRequired[str]
    author: NotRequired[str]

class Collaboration(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    parent_organisation: NotRequired[str]
    child_organisation: NotRequired[str]
    principal_investigator_contribution: NotRequired[str]
    partner_contribution: NotRequired[str]
    start: NotRequired[date]
    end: NotRequired[date]
    sector: NotRequired[str]
    country: NotRequired[str]
    impact: NotRequired[str]
    supporting_url: NotRequired[str]

class Dissemination(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    form: NotRequired[str]
    primary_audience: NotRequired[str]
    years_of_dissmemination: NotRequired[str]
    results: NotRequired[str]
    impact: NotRequired[str]
    type_of_presentation: NotRequired[str]
    geographic_reach: NotRequired[str]
    part_of_official_scheme: NotRequired[bool]
    supporting_url: NotRequired[str]

class FurtherFunding(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    narrative: NotRequired[str]
    amount: NotRequired[ValuePounds]
    organisation: NotRequired[str]
    department: NotRequired[str]
    funding_id: NotRequired[str]
    start: NotRequired[date]
    end: NotRequired[date]
    sector: NotRequired[str]
    country: NotRequired[str]

class Exploitation(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    type: NotRequired[str]
    method: NotRequired[str]
    other_involvement: NotRequired[str]
    ip_exploited: NotRequired[bool]
    start: NotRequired[date]

class ImpactSummary(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    impact_types: NotRequired[List[str]]
    summary: NotRequired[str]
    beneficiaries: NotRequired[str]
    contribution_method: NotRequired[str]
    sector: NotRequired[str]
    first_year_of_impact: int

class IntellectualProperty(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    protection: NotRequired[str]
    patent_id: NotRequired[str]
    year_protection_granted: int
    type: NotRequired[str]
    impact: NotRequired[str]
    licensed: NotRequired[str]
    patent_url: NotRequired[str]
    start: NotRequired[date]
    end: NotRequired[date]

class PolicyInfluence(TypedDict):
    influence: NotRequired[str]
    type: NotRequired[str]
    guideline_title: NotRequired[str]
    impact: NotRequired[str]
    methods: NotRequired[str]
    areas: NotRequired[List[str]]
    geographic_reach: NotRequired[str]
    supporting_url: NotRequired[str]

class Product(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    type: NotRequired[str]
    stage: NotRequired[str]
    status: NotRequired[str]
    clinical_trial: NotRequired[bool]
    ukcrn_isctn_id: NotRequired[str]
    year_development_completed: NotRequired[int]
    impact: NotRequired[str]
    supporting_url: NotRequired[str]

class ResearchMaterial(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    type: NotRequired[str]
    impact: NotRequired[str]
    software_developed: NotRequired[bool]
    software_open_sourced: NotRequired[bool]
    provided_to_others: NotRequired[bool]
    year_first_provided: NotRequired[int]
    supporting_url: NotRequired[str]

class ArtisticAndCreativeProduct(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    type: NotRequired[str]
    impact: NotRequired[str]
    year_first_provided: NotRequired[int]
    supporting_url: NotRequired[str]

class ResearchDatabaseAndModel(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    type: NotRequired[str]
    impact: NotRequired[str]
    provided_to_others: NotRequired[bool]
    year_first_provided: NotRequired[str]
    supporting_url: NotRequired[str]

class SoftwareAndTechnicalProduct(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    type: NotRequired[str]
    impact: NotRequired[str]
    software_open_sourced: NotRequired[bool]
    open_source_license: NotRequired[bool]
    provided_to_others: NotRequired[bool]
    year_first_provided: NotRequired[int]
    supporting_url: NotRequired[str]

class SpinOut(TypedDict):
    description: NotRequired[str]
    company_name: NotRequired[str]
    company_description: NotRequired[str]
    impact: NotRequired[str]
    website: NotRequired[str]
    registration_number: NotRequired[str]
    year_established: NotRequired[str]
    ip_exploited: NotRequired[bool]
    joint_venture: NotRequired[bool]

class OtherResearchItem(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    type: NotRequired[str]
    sub_title: NotRequired[str]
    series_title: NotRequired[str]
    series_number: NotRequired[str]
    other_information: NotRequired[str]
    edition: NotRequired[str]
    doi: NotRequired[str]
    publisher: NotRequired[str]
    supporting_url: NotRequired[str]

#######


class PeopleResponse(Response):
    person: List[Person]


class ProjectsResponse(Response):
    project: List[Project]


class OrganisationsResponse(Response):
    organisation: List[Organisation]


class FundsResponse(Response):
    fund: List[Fund]

class OutcomesResponse(Response):
    artistic_and_creative_product: List[ArtisticAndCreativeProduct]
    collaboration: List[Collaboration]
    dissemination: List[Dissemination]
    exploitation: List[Exploitation]
    further_funding: List[FurtherFunding]
    impact_summary: List[ImpactSummary]
    intellectual_property: List[IntellectualProperty]
    key_finding: List[KeyFinding]
    other_research_item: List[OtherResearchItem]
    policy_influence: List[PolicyInfluence]
    product: List[Product]
    publication: List[Publication]
    research_database_and_model: List[ResearchDatabaseAndModel]
    research_material: List[ResearchMaterial]
    software_and_technical_product: List[SoftwareAndTechnicalProduct]
    spin_out: List[SpinOut]