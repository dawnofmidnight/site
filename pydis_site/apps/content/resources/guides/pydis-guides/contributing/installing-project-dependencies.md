---
title: Installing Project Dependencies
description: A guide to installing the dependencies of our projects.
icon: fab fa-python
---

> **Note:** The process varies depending on your choice of code editor / IDE, so refer to one of the following guides:

- [Installing dependencies with PyCharm](#installing-dependencies-with-pycharm)
- [Installing dependencies with the command line](#installing-dependencies-with-the-command-line)

The following will use the [Sir-Lancebot](https://github.com/python-discord/sir-lancebot/) repository as an example, but the steps are the same for all other repositories.
You should have already cloned your fork as described in [**Cloning a Repository**](../cloning-repository).

---

## Installing dependencies with PyCharm
1. Load up your project in PyCharm.
2. Go to the Project Settings by clicking `File`, then `Settings...`. Alternatively, use the shortcut key `Ctrl+Alt+S`.
3. Navigate to `Project Interpreter`, then click the gear icon and click `Add`.
![PyCharm Interpreter Settings](/static/images/wiki/contributing/pycharm_interpreter.png)
4. In the popup window, click `Pipenv Environment`, make sure `Install packages from Pipfile` is checked, then click `OK`.
![PyCharm Pipenv Environment](/static/images/wiki/contributing/pycharm_pipenv.png)
5. PyCharm will automatically install the packages required into a virtual environment.
![PyCharm Project Interpreter](/static/images/wiki/contributing/pycharm_pipenv_success.png)

---

## Installing dependencies with the command line
1. Make sure you are in the project directory.
2. Install project and development dependencies:
```shell
$ pipenv sync --dev
```
* Remember to also set up pre-commit hooks to ensure your pushed commits will never fail linting:
```shell
$ pipenv run precommit
```
