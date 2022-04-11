from gtr import GtR2Client, ProjectsQuery
from pprint import pprint

gtr = GtR2Client(debug=True)

"""
query:  = {
    "page_size": 10,
    "query": "Manufacturing"
}
"""

funds = gtr.get_funds()

pprint(funds["fund"][0])
