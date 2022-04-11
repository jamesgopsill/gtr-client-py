from gtr import GtR2Client, PeopleQuery
from pprint import pprint

gtr = GtR2Client(debug=True)

people = gtr.get_people()

pprint(people["size"])
pprint(people["person"][0])

query: PeopleQuery = {"page_size": 10}

people = gtr.get_people(query)

pprint(people.keys())
pprint(people["person"][0])
