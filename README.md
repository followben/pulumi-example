# Multi-project Pulumi Example

This repo demonstrates a monorepo setup with multiple pulumi projects, incl. difficulties with importing python packages/ modules outside a pulumi project directory

## Requirements

- AWS credentials in env
- Pulumi CLI installed
- Python 3.6+

## Getting started

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run for stack1 (a python package):

```sh
cd infra/stack1
pulumi preview
```

Select the `dev` stack and observe the error:

```
ModuleNotFoundError: No module named 'infra'
```

The same thing will occur for stack2, which is not a package and doesn't specify a venv in Pulumi.yaml.