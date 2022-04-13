from gtr import GtR2Client, ProjectsQuery
from pprint import pprint

gtr = GtR2Client(debug=True)

query: ProjectsQuery = {
    "page_size": 10, 
    "query": "manufacturing"
}

projects = gtr.projects(query)

for project in projects["project"]:
    
    pprint(project["title"], depth=1)
    
    orgs = gtr.project_organisations(project["id"])
    pprint(orgs["organisation"][0], depth=1)
    
    people = gtr.project_persons(project["id"])
    pprint(people["person"][0], depth=1)
    
    break