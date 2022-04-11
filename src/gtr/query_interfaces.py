from typing import TypedDict, List
from typing_extensions import NotRequired
import enum


class SortOrder(enum.Enum):
    ASCENDING = "A"
    DESCENDING = "D"


class PeopleSearchFields(enum.Enum):
    FIRST_NAME = "per.fn"
    FAMILY_NAME = "per.sn"
    FIRST_NAME_FAMILY_NAME = "per.fnsn"
    ORCID_ID = "per.orcidId"
    ORGANISATION_NAME = "per.org.n"
    PROJECT_TITLES = "per.pro.t"
    PROJECT_ABCSTRACTS = "per.pro.abs"


class PeopleSortFields(enum.Enum):
    FIRST_NAME = "per.fn"
    FAMILY_NAME = "per.sn"
    RELEVANCE = "score"


class ProjectSearchFields(enum.Enum):
    PROJECT_REFERENCE = "pro.gr"
    PROJECT_TITLE = "pro.t"
    PROJECT_ABSTRACT = "pro.a"
    ORCID_ID = "pro.orcidId"
    RESEARCH_TOPICS = "pro.rt"
    HEALTH_ACTIVITIES = "pro.ha"
    RCUK_PROGRAMMES = "pro.rcukp"
    LEAD_FUNDER_NAME = "pro.lf"


class ProjectSortFields(enum.Enum):
    START_DATE = "pro.sd"
    END_DATE = "pro.ed"
    FUNDED_VALUE = "pro.am"
    RELEVANCE = "score"


class OrganisationSearchFields(enum.Enum):
    ORGANISATION_NAME = "org.n"
    PROJECT_TITLES = "org.pro.t"
    ORCID_ID = "org.orcidId"
    PROJECT_ABCSTRACTS = "org.pro.a"


class OrganisationSortFields(enum.Enum):
    ORGANISATION_NAME = "org.n"
    RELEVANCE = "score"


class FundsSearchFields(enum.Enum):
    FUNDED_PROJECT_TITLE = "fu.pro.t"
    FUND_AMOUNT = "fu.am"
    FUNDER_ORGANISATION_NAME = "fu.org.n"
    FUND_TYPE = "fu.ty"


class FundsSortFields(enum.Enum):
    FUND_START_DATE = "fu.sd"
    FUND_END_DATE = "fu.ed"
    FUND_AMOUNT = "fu.am"
    FUND_TYPE = "fu.ty"
    RELEVANCE = "score"

class OutcomesSortFields():
    RELEVANCE = "score" 

#############


class Query(TypedDict):
    query: NotRequired[str]
    page: NotRequired[int]
    page_size: NotRequired[int]
    sort_order: NotRequired[SortOrder]


class PeopleQuery(Query):
    search_fields: NotRequired[List[PeopleSearchFields]]
    sort_fields: NotRequired[PeopleSortFields]


class ProjectsQuery(Query):
    search_fields: NotRequired[List[ProjectSearchFields]]
    sort_fields: NotRequired[ProjectSortFields]


class OrganisationsQuery(Query):
    search_fields: NotRequired[List[OrganisationSearchFields]]
    sort_fields: NotRequired[OrganisationSortFields]


class FundsQuery(Query):
    search_fields: NotRequired[List[FundsSearchFields]]
    sort_fields: NotRequired[FundsSortFields]

class Outcomes(Query):
    sort_fields: NotRequired[OutcomesSortFields]