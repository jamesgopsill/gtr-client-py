# A python package for the GtR API


## Development

```
python -m venv .venv
```

**Mac / Linux**

```
source .venv/bin/activate
```

**Windows (Powershell)**

```
.venv/Scripts/activate.ps1
```

```
pip install -r requirements_dev.txt
```

Install the package within your local dev environment.

```
pip install -e .
```

- https://packaging.python.org/en/latest/tutorials/installing-packages/#id25
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- https://realpython.com/lessons/production-vs-development-dependencies/
- https://towardsdatascience.com/whats-init-for-me-d70a312da583

## Documentation

```
pdoc ./docs ./src/gtr
```

- https://pdoc.dev/

## Formatting

```
black src/
```

- https://github.com/psf/black

## Testing

```
python -m unittest -v
```


## Useful Links

- https://stackoverflow.com/questions/17156078/converting-identifier-naming-between-camelcase-and-underscores-during-json-seria