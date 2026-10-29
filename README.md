# Python Environment Variable Exercise

A small coursework example demonstrating configuration loading with `python-dotenv`.

## Contents

- [Python_exam.py](Python_exam.py): loads `MAIN_KEY` and `SECRET_KEY` and reports whether both are present.
- `requirements.txt`: currently empty.

## Run with sample values

```bash
python -m venv .venv
python -m pip install python-dotenv
python Python_exam.py
```

Activate the environment before installation. Provide local environment variables or a local `.env` file containing fictional values:

```dotenv
MAIN_KEY=example-main
SECRET_KEY=example-secret
```

## Configuration handling

The current script prints the loaded values. Use dummy values when running this exercise. The repository also tracks a `.env` file; real credentials should be kept outside version control and should never be included in screenshots or logs.

This is a configuration-loading demonstration, with no external API integration.
