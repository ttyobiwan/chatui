# 📬 chatui

[![python](https://img.shields.io/static/v1?label=python&message=3.11&color=informational&logo=python&logoColor=white)](https://www.python.org/)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)

![chatui cover](.github/static/chatui.png)

## 📝 Table of Contents

- [About](#about)
- [Installation](#installation)

## 📖 About <a name = "about"></a>

In-terminal ChatGPT powered by Textual.

## 💾 Installation <a name = "installation"></a>

Create a new virtual environment (assuming you already have Python installed e.g. via `pyenv`)

```bash
python -m venv venv
```

Activate it

```bash
source ./venv/bin/activate
```

Install requirements for local setup

```bash
pip install -r ./requirements/dev.txt
```

Get your OpenAI API key ([link](https://platform.openai.com/account/api-keys)) and set it as an environment variable

```bash
export OPENAI_KEY=<key>
```

You now be able to run the project

```bash
make run
```
