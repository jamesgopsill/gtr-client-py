from msilib import schema
from gtr import GtR2Client
from pprint import pprint

gtr = GtR2Client(debug=True)

schema = gtr.schema("")

pprint(schema)
