# A python package for the GtR API

This client is a fully-typed python client for the [UKRI's Gateway to Research API](https://gtr.ukri.org/).

## Getting Started

I haven't put the package on pypi just yet so installing the package requires installing it from the repo.

```
pip install git+https://github.com/jamesgopsill/gtr-client-py.git#egg=gtr
```

- https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github

You can then use it in your python code like so:

```python
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
```

For more examples, please see the [`examples`](./examples) folder.

## Development

I would recommend creating a virtual environment for development work.

```
python -m venv .venv
```

Then activate it using.

**Mac / Linux**

```
source .venv/bin/activate
```

**Windows**

```
.venv/Scripts/activate
```

Then install the development requirements.

```
pip install -r requirements_dev.txt
```

And then install the package within your local virtual dev environment.

```
pip install -e .
```

- https://packaging.python.org/en/latest/tutorials/installing-packages/#id25
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- https://realpython.com/lessons/production-vs-development-dependencies/
- https://towardsdatascience.com/whats-init-for-me-d70a312da583

## Documentation

Documentation is generated using:

```
pdoc ./src/gtr
```

If you want to run it on a localhost server for development.

**or**

```
pdoc ./src/gtr -o ./docs
```

To write new docs to the repo.

- https://pdoc.dev/

## Formatting

And we format the code using black.

```
black src/
```

- https://github.com/psf/black

## Testing

Testing uses unittest.

```
python -m unittest -v
```


## Useful Links

- https://stackoverflow.com/questions/17156078/converting-identifier-naming-between-camelcase-and-underscores-during-json-seria