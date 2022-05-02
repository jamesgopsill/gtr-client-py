from typing import TypedDict, List, Any
from datetime import date


class Response(TypedDict):
    """
    The base response class.
    """
    size: int
    """"""
    total_pages: int
    """"""
    total_size: int
    """"""
    page: int


class Link(TypedDict):
    """"""
    href: str
    """"""
    rel: str
    """"""
    start: date
    """"""
    end: date
    """"""
    other_attributes: Any


class Links(TypedDict):
    """"""
    link: List[Link]
    """"""


class Identifier(TypedDict):
    """"""
    value: str
    """"""
    type: str
    """"""

class Identifiers(TypedDict):
    """"""
    identifiers: List[Identifier]
    """"""


class HealthCategory(TypedDict):
    """"""
    id: str
    """"""
    text: str
    """"""


class HealthCategories(TypedDict):
    """"""
    health_category: List[HealthCategory]
    """"""


class ResearchSubject(TypedDict):
    """"""
    id: str
    """"""
    text: str
    """"""
    percentage: int
    """"""


class ResearchSubjects(TypedDict):
    """"""
    researcSubject: List[ResearchSubject]
    """"""


class ResearchTopic(TypedDict):
    """"""
    id: str
    """"""
    text: str
    """"""

class ResearchTopics(TypedDict):
    """"""
    research_topics: List[ResearchTopic]
    """"""

class Participant(TypedDict):
    """"""
    grant_offer: float
    """"""
    organisation_id: str
    """"""
    organisation_name: str
    """"""
    project_cost: float
    """"""
    role: str
    """"""

class ParticipantValues(TypedDict):
    """"""
    participant: List[Participant]
    """"""


class Address(TypedDict):
    """"""
    city: str
    """"""
    created: date
    """"""
    id: str
    """"""
    line1: str
    """"""
    post_code: str
    """"""
    region: str
    """"""
    type: str


class Addresses(TypedDict):
    """"""
    address: List[Address]
    """"""


class ValuePounds(TypedDict):
    """"""
    currencyCode: str
    """"""
    amount: float
    """"""


######


class Person(TypedDict, total=False):
    """A person on Gateway to Research."""
    links: Links
    """"""
    id: str
    """"""
    href: str
    """"""
    created: str
    """"""
    first_name: str
    """"""
    other_names: str
    """"""
    surname: str
    """"""
    orcid_id: str
    """"""


class Project(TypedDict, total=False):
    """A project on Gateway to Research."""
    links: Links
    """"""
    id: str
    """"""
    href: str
    """"""
    created: date
    """"""
    identifiers: Identifiers
    """"""
    title: str
    """"""
    status: str
    """"""
    grant_category: str
    """"""
    lead_funder: str
    """"""
    lead_organisation_department: str
    """"""
    abstract_text: str
    """"""
    health_categories: HealthCategories
    """"""
    research_activities: Any
    """"""
    research_subjects: ResearchSubjects
    """"""
    research_topics: ResearchTopics
    """"""
    rcuk_programmes: Any
    """"""
    participant_values: ParticipantValues
    """"""

class Organisation(TypedDict, total=False):
    """An organisation on Gateway to Research."""
    links: Links
    """"""
    addresses: Addresses
    """"""
    href: str
    """"""
    id: str
    """"""
    name: str
    """"""


class Fund(TypedDict, total=False):
    """A fund on Gateway to Research."""
    links: Links
    """"""
    id: str
    """"""
    href: str
    """"""
    created: date
    """"""
    start: date
    """"""
    end: date
    """"""
    valuePounds: ValuePounds
    """"""
    category: str
    """"""
    created: str


class KeyFinding(TypedDict, total=False):
    """A key finding on Gateway to Research."""
    description: str
    """"""
    non_academic_uses: str
    """"""
    exploitation_pathways: str
    """"""

class Publication(TypedDict, total=False):
    """A publication on Gateway to Research."""
    title: str
    """"""
    type: str
    """"""
    abstract_text: str
    """"""
    other_information: str
    """"""
    journal_title: str
    """"""
    date_published: date
    """"""
    publication_url: str
    """"""
    pub_med_id: str
    """"""
    isbn: str
    """"""
    issn: str
    """"""
    series_number: str
    """"""
    series_title: str
    """"""
    sub_title: str
    """"""
    volume_title: str
    """"""
    doi: str
    """"""
    volume_number: str
    """"""
    issue: str
    """"""
    total_pages: str
    """"""
    edition: str
    """"""
    chapter_number: str
    """"""
    chapter_title: str
    """"""
    page_reference: str
    """"""
    conference_event: str
    """"""
    conference_location: str
    """"""
    conference_number: str
    """"""
    author: str
    """"""


class Collaboration(TypedDict, total=False):
    """A collaboration on Gateway to Research."""
    title: str
    """"""
    description: str
    """"""
    parent_organisation: str
    """"""
    child_organisation: str
    """"""
    principal_investigator_contribution: str
    """"""
    partner_contribution: str
    """"""
    start: date
    """"""
    end: date
    """"""
    sector: str
    """"""
    country: str
    """"""
    impact: str
    """"""
    supporting_url: str
    """"""

class Dissemination(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    form: str
    """"""
    primary_audience: str
    """"""
    years_of_dissmemination: str
    """"""
    results: str
    """"""
    impact: str
    """"""
    type_of_presentation: str
    """"""
    geographic_reach: str
    """"""
    part_of_official_scheme: bool
    """"""
    supporting_url: str
    """"""

class FurtherFunding(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    narrative: str
    """"""
    amount: ValuePounds
    """"""
    organisation: str
    """"""
    department: str
    """"""
    funding_id: str
    """"""
    start: date
    """"""
    end: date
    """"""
    sector: str
    """"""
    country: str
    """"""

class Exploitation(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    type: str
    """"""
    method: str
    """"""
    other_involvement: str
    """"""
    ip_exploited: bool
    """"""
    start: date
    """"""

class ImpactSummary(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    impact_types: List[str]
    """"""
    summary: str
    """"""
    beneficiaries: str
    """"""
    contribution_method: str
    """"""
    sector: str
    """"""
    first_year_of_impact: int
    """"""

class IntellectualProperty(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    protection: str
    """"""
    patent_id: str
    """"""
    year_protection_granted: int
    """"""
    type: str
    """"""
    impact: str
    """"""
    licensed: str
    """"""
    patent_url: str
    """"""
    start: date
    """"""
    end: date
    """"""


class PolicyInfluence(TypedDict, total=False):
    """"""
    influence: str
    """"""
    type: str
    """"""
    guideline_title: str
    """"""
    impact: str
    """"""
    methods: str
    """"""
    areas: List[str]
    """"""
    geographic_reach: str
    """"""
    supporting_url: str
    """"""

class Product(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    type: str
    """"""
    stage: str
    """"""
    status: str
    """"""
    clinical_trial: bool
    """"""
    ukcrn_isctn_id: str
    """"""
    year_development_completed: int
    """"""
    impact: str
    """"""
    supporting_url: str
    """"""


class ResearchMaterial(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    type: str
    """"""
    impact: str
    """"""
    software_developed: bool
    """"""
    software_open_sourced: bool
    """"""
    provided_to_others: bool
    """"""
    year_first_provided: int
    """"""
    supporting_url: str
    """"""


class ArtisticAndCreativeProduct(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    type: str
    """"""
    impact: str
    """"""
    year_first_provided: int
    """"""
    supporting_url: str
    """"""


class ResearchDatabaseAndModel(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    type: str
    """"""
    impact: str
    """"""
    provided_to_others: bool
    """"""
    year_first_provided: str
    """"""
    supporting_url: str
    """"""


class SoftwareAndTechnicalProduct(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    type: str
    """"""
    impact: str
    """"""
    software_open_sourced: bool
    """"""
    open_source_license: bool
    """"""
    provided_to_others: bool
    """"""
    year_first_provided: int
    """"""
    supporting_url: str
    """"""


class SpinOut(TypedDict, total=False):
    """"""
    description: str
    """"""
    company_name: str
    """"""
    company_description: str
    """"""
    impact: str
    """"""
    website: str
    """"""
    registration_number: str
    """"""
    year_established: str
    """"""
    ip_exploited: bool
    """"""
    joint_venture: bool
    """"""


class OtherResearchItem(TypedDict, total=False):
    """"""
    title: str
    """"""
    description: str
    """"""
    type: str
    """"""
    sub_title: str
    """"""
    series_title: str
    """"""
    series_number: str
    """"""
    other_information: str
    """"""
    edition: str
    """"""
    doi: str
    """"""
    publisher: str
    """"""
    supporting_url: str
    """"""


#######


class PeopleResponse(Response):
    """"""
    person: List[Person]
    """"""

class ProjectsResponse(Response):
    """"""
    project: List[Project]
    """"""

class OrganisationsResponse(Response):
    """"""
    organisation: List[Organisation]
    """"""

class FundsResponse(Response):
    """"""
    fund: List[Fund]
    """"""

class OutcomesResponse(Response):
    """"""
    artistic_and_creative_product: List[ArtisticAndCreativeProduct]
    """"""
    collaboration: List[Collaboration]
    """"""
    dissemination: List[Dissemination]
    """"""
    exploitation: List[Exploitation]
    """"""
    further_funding: List[FurtherFunding]
    """"""
    impact_summary: List[ImpactSummary]
    """"""
    intellectual_property: List[IntellectualProperty]
    """"""
    key_finding: List[KeyFinding]
    """"""
    other_research_item: List[OtherResearchItem]
    """"""
    policy_influence: List[PolicyInfluence]
    """"""
    product: List[Product]
    """"""
    publication: List[Publication]
    """"""
    research_database_and_model: List[ResearchDatabaseAndModel]
    """"""
    research_material: List[ResearchMaterial]
    """"""
    software_and_technical_product: List[SoftwareAndTechnicalProduct]
    """"""
    spin_out: List[SpinOut]
    """"""


class KeyFindingsResponse(Response):
    """"""
    key_finding: List[KeyFinding]
    """"""

class ImpactSummariesResponse(Response):
    """"""
    impact_summary: List[ImpactSummary]
    """"""

class PublicationsResponse(Response):
    """"""
    publication: List[Publication]
    """"""

class CollaborationsResponse(Response):
    """"""
    collaborations: List[Collaboration]
    """"""

class IntellectualPropertiesResponse(Response):
    """"""
    intellectual_property: List[IntellectualProperty]
    """"""

class PolicyInfluencesResponse(Response):
    """"""
    policy_influence: List[PolicyInfluence]
    """"""

class ProductsResponse(Response):
    """"""
    products: List[Product]
    """"""

class ResearchMaterialsResponse(Response):
    """"""
    research_material: List[ResearchMaterial]
    """"""

class SpinOutResponse(Response):
    """"""
    spin_out: List[SpinOut]
    """"""

class FurtherFundingsResponse(Response):
    """"""
    further_funding: List[FurtherFunding]
    """"""

class DisseminationsResponse(Response):
    """"""
    dissemination: List[Dissemination]
    """"""