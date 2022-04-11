from gtr import GtR2Client
from pprint import pprint

gtr = GtR2Client(debug=True)

funds = gtr.funds()

pprint(funds["fund"][0])
