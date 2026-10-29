# Python Environment Variable Exercise

A small coursework example demonstrating configuration loading with `python-dotenv`.

## Contents

- [Python_exam.py](Python_exam.py): loads `MAIN_KEY` and `SECRET_KEY` and reports whether both are present.
- [requirements.txt](requirements.txt): runtime dependency.
- [.env.example](.env.example): dummy configuration template.

## Run with sample values

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python Python_exam.py
```

Activate the environment before installation. Provide local environment variables or a local `.env` file containing fictional values:

```dotenv
MAIN_KEY=example-main
SECRET_KEY=example-secret
```

Copy `.env.example` to `.env` for local sample configuration. Configuration is resolved beside the script, so launching from another directory works.

## Configuration handling

The script reports success or missing variable names without printing their values. It exits with status 1 when required values are missing. Use dummy values when running this exercise. The repository still tracks its original `.env` file; `.gitignore` prevents new untracked environment files from being added, but does not remove the existing file from Git history. real credentials should be kept outside version control and should never be included in screenshots or logs.

This is a configuration-loading demonstration, with no external API integration.

## Regression checks

```bash
python -m unittest discover -s tests -v
```
