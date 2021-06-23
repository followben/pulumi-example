# Multi-project Pulumi Example

This repo demonstrates a monorepo setup with multiple pulumi projects, incl. difficulties with importing python packages/ modules outside a pulumi project directory

## Requirements

- AWS credentials in env
- Pulumi CLI installed
- Python 3.6+

## Getting started

In the root of the project, run:

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To preview project1, from the root of the project run `pulumi -C src/infra/project1 preview`.

Select the `dev` stack and observe the error:

```
...
File "./__main__.py", line 6, in <module>
        from infra.lib import example
    ModuleNotFoundError: No module named 'infra'
```

Observe the same for project2 (which differs in that it's not a python package and it doesn't specify a venv in Pulumi.yaml).