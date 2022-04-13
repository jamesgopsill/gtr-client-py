from gtr import GtR2Client, PeopleQuery
from pprint import pprint

gtr = GtR2Client(debug=True)

people = gtr.people()

pprint(people["size"])
pprint(people["person"][0])

query: PeopleQuery = {
    "page_size": 10
}

people = gtr.people(query)

pprint(people.keys())
pprint(people["person"][0])
