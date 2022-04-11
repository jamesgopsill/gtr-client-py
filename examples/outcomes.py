from gtr import GtR2Client
from pprint import pprint

gtr = GtR2Client(debug=True)

outcomes = gtr.outcomes()

pprint(outcomes, depth=2)
