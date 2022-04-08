from gtr import GtR2Client, ProjectsQuery
from pprint import pprint

gtr = GtR2Client(debug=True)

query: ProjectsQuery = {
    "page_size": 10,
    "query": "Manufacturing"
}

projects = gtr.get_projects(query)

for project in projects["project"]:
    pprint(project["title"])
    orgs = gtr.get_project_organisations(project["id"])
    pprint(orgs)
    break