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

## Demonstrating [the import issue](https://github.com/pulumi/pulumi/issues/7360)

To preview project1, from the root of the project run `pulumi -C src/infra/project1 preview`.

Select the `dev` stack and observe the error:

```
...
File "./__main__.py", line 6, in <module>
        from infra.lib import example
    ModuleNotFoundError: No module named 'infra'
```

### Workaround


Preview project2 from the root of the project by running `pulumi -C src/infra/project2 preview`.

This works thanks to a hack at the top of `__main__.py` which adds the src directory to the syspath.