from gtr import GtR2Client, ProjectsQuery
from pprint import pprint

gtr = GtR2Client(debug=True)

query: ProjectsQuery = {
    "page_size": 10, 
    "query": "Manufacturing"
}

projects = gtr.get_projects(query)

for project in projects["project"]:
    
    pprint(project, depth=1)
    
    orgs = gtr.project_organisations(project["id"])
    pprint(orgs["organisation"][0], depth=1)
    
    people = gtr.project_persons(project["id"])
    pprint(people["person"][0], depth=1)
    
    break
