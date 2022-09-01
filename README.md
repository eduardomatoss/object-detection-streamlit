# object-detection-streamlit

Project responsible for simulating a simple form of a bank with the recognition of people and objects

[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3813/) 
[![PEP20](https://img.shields.io/badge/code%20style-pep20-red.svg)](https://www.python.org/dev/peps/pep-0020/) 
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/) 
[![bandit](https://img.shields.io/badge/code%20style-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Technology and Resources

- [Python 3.8](https://www.python.org/downloads/release/python-3813/) - **pre-requisite**
- [Docker](https://www.docker.com/get-started) - **pre-requisite**
- [Docker Compose](https://docs.docker.com/compose/) - **pre-requisite**
- [Pipenv](https://github.com/pypa/pipenv)
- [Streamlit](https://streamlit.io)

*Please pay attention on **pre-requisites** resources that you must install/configure.*

### How to Install

```
make local/install
```

### How to Build

```
make docker/build
```

### How to Run

```
make local/run
make docker/run
```

### How to Test

```
make local/test
make docker/test
```

### How to lint

`make docker/lint` or `make local/lint` to lint

`make docker/bandit` or `make local/bandit` to execute the bandit check

`make docker/check-packages` or `make local/check-packages` to check for packages vulnerabilities

**Helpful commands**

*Please, check all available commands in the [Makefile](Makefile) for more information*.

## Extras infos

- If you use the [vscode](https://code.visualstudio.com/) editor we have some examples of [launch.json](.docs/vscode.md) to speed up your tests.
