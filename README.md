# configtemplate

This is a tiny configuration templating script using Python's jinja2. It operates
in a similar manner to a configuration management system insofar as it provides a
hierarchical view of data which can be overriden.

## Template Syntax

See: https://jinja.palletsprojects.com/en/2.11.x/templates/

## Examples

Read in a single `.yml` file and render a template  called `template.in.yml`:

```bash
$ python template.py --file=variables.yml template.in.yml
```

Read all the `.yml` files in the directory `data/variables` and render a template:

```bash
$ python template.py --dir=data/variables template.in.yml
```

Read all the files in for a directory and then override some values:

```bash
$ python template.py --dir=data/variables --file=overrides.yml template.in.yml
```

## Requirements

For use, just the docker image.

For development:
* (Python)[https://www.python.org/]
* (bats)[https://github.com/bats-core/bats-core]
* (Docker)[https://www.docker.com/]
