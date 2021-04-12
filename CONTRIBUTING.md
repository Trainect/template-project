# Table of Contents

- [Contributing to Template Project](#contributing-to-template-project)
- [Download this Repository](#download-this-repository)
- [Virtual Environment](#virtual-environment)
  - [Create the Virtual Environment](#create-the-virtual-environment)
  - [Activate the Virtual Environment](#activate-the-virtual-environment)
    - [Windows](#windows)
    - [Unix or MacOS](#unix-or-macos)
- [IDE Installation and Configuration](#ide-installation-and-configuration)
  - [VS Code Installation](#vs-code-installation)
  - [VS Code Configuration](#vs-code-configuration)
- [Development Installation](#development-installation)
  - [Windows](#windows)
  - [Unix or MacOS](#unix-or-macos)
- [Our Development Process](#our-development-process)
  - [Code Style](#code-style)
  - [Type Hints](#type-hints)
  - [Pre-Commit Git Hooks](#pre-commit-git-hooks)
    - [Enabling Pre-Commit Hooks](#enabling-pre-commit-hooks)
    - [Update the Hooks Version](#update-the-hooks-version)
  - [Unit Tests](#unit-tests)
    - [Test Coverage Reports](#test-coverage-reports)
  - [Comments and Docstrings](#comments-and-docstrings)
  - [Documentation](#documentation)
    - [How to Build the Documentation](#how-to-build-the-documentation)
    - [Deploying the Documentation on Confluence](#deploying-the-documentation-on-confluence)
- [Our Source-Control Branching Model](#our-source-control-branching-model)
  - [Trunk-Based Development](#trunk-based-development])
  - [The Flow](#the-flow])
  - [Additional Best Practices](#additional-best-practices)

## Contributing to Template Project

If you want to contribute to Template Project, be sure to read all the guidelines in this document and set up your development environment as described in the following sections.

> **Note**: We use Python 3 (and you should do the same). Whenever you see `python`, if your computer is set to Python 2, you need to replace it with` python3`.

## Download this Repository

First, you need to clone this repository, find out how to do it [here](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone?utm_campaign=learn-git-clone&utm_medium=in-app-help&utm_source=stash).

## Virtual Environment

We use [venv](https://docs.python.org/3/library/venv.html) for creating lightweight "virtual environments".

### Create the Virtual Environment

To create a virtual environment for this project run the commands related to your operating system.
#### Windows

```bash
cd template-project  # Only if you are not already in the project folder
python -m venv venv\\template-project
```

#### Unix or MacOS

```bash
cd template-project  # Only if you are not already in the project folder
python -m venv venv/template-project
```

### Activate the Virtual Environment

To activate the virtual environment of this project run the commands related to your operating system.

#### Windows

To activate it on Windows run:
```bash
venv\\template-project\\Scripts\\activate.bat
```

#### Unix or MacOS

```bash
source venv/template-project/bin/activate
```

## IDE Installation and Configuration

### VS Code Installation

Before you start to develop and collaborate on this project, you should **install an IDE**. ([What is a IDE?](https://en.wikipedia.org/wiki/Integrated_development_environment)). We strongly recommend downloading [VS Code](https://code.visualstudio.com/download).

### VS Code Configuration

Create or modify the `settings.json` file in the `.vscode` folder as follows:

#### Windows

```
{
    "editor.formatOnSave": true,
    "files.autoSave": "afterDelay",
    "files.insertFinalNewline": true,
    "files.trimTrailingWhitespace": true,
    "python.formatting.provider": "black",
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
    "python.linting.mypyEnabled": true,
    "python.pythonPath": "venv\\template-project\\Scripts\\python.exe",
    "python.sortImports.args": [
        "-sp isort.cfg" // points to isort config file
    ],
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    }
}
```

#### Unix or MacOS

```
{
    "editor.formatOnSave": true,
    "files.autoSave": "afterDelay",
    "files.insertFinalNewline": true,
    "files.trimTrailingWhitespace": true,
    "python.formatting.provider": "black",
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
    "python.linting.mypyEnabled": true,
    "python.pythonPath": "venv/template-project/bin/python",
    "python.sortImports.args": [
        "-sp isort.cfg" // points to isort config file
    ],
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    }
}
```

## Development Installation

To get the development installation with all the necessary dependencies for linting, testing, and building the documentation, run the commands related to your operating system.

### Windows

```bash
cd template-project  # Only if you are not already in the project folder
venv\\template-project\\Scripts\\activate.bat
pip install -e .[dev]
pre-commit install
```

### Unix or MacOS

```bash
cd template-project  # Only if you are not already in the project folder
source venv/template-project/bin/activate
pip install -e .\[dev\]
pre-commit install
```

## Our Development Process

### Code Style

Template Project uses [black](https://github.com/ambv/black) and  [flake8](https://github.com/PyCQA/flake8) to enforce a common code style across the code base. black and flake8 are installed easily via pip using `pip install black flake8` (not necessary if previously installed with `pip install -e .[dev]`), and run locally by calling
```bash
black .
flake8 .
```
from the repository root. No additional configuration should be needed (see the [black documentation](https://black.readthedocs.io/en/stable/installation_and_usage.html#usage) for advanced usage).

Template Project also uses [isort](https://github.com/timothycrosley/isort) to sort imports alphabetically and separate into sections. isort is installed easily via pip using `pip install isort` (not necessary if previously installed with `pip install -e .[dev]`), and run locally by calling
```bash
isort .
```
from the repository root. Configuration for isort is located in .isort.cfg.

We feel strongly that having a consistent code style is extremely important, therefore a PR will not be accepted if it does not adhere to the black or flake8 formatting style or isort import ordering.

### Type Hints

Template Project is fully typed using python 3.6+ [type hints](https://www.python.org/dev/peps/pep-0484/). We expect any contributions to also use proper type annotations, and we enforce consistency of these in our continuous integration tests.

To type check your code locally, install [mypy](https://github.com/python/mypy), which can be done with pip using `pip install "mypy>=0.760"` (not necessary if previously installed with `pip install -e .[dev]`). Then run this script from the repository root:
```bash
./scripts/run_mypy.sh
```
Note that we expect mypy to have version 0.760 or higher, and when type checking, use PyTorch 1.4 or higher due to fixes to PyTorch type hints available in 1.4. We also use the Literal feature which is available only in Python 3.8 or above. If type-checking using a previous version of Python, you will need to install the typing-extension package which can be done with pip using `pip install typing-extensions` (not necessary if you followed the previous installation).

### Pre-Commit Git Hooks

We use client-side pre-commit [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) to launch a series of automatic code style checks when a developer attempts a commit to the repository.

If any of the checks fail Git will prevent the commit, printing a log of the reasons for failing, and in some cases modifying automatically the files and saving them in the unstaged area for user validation.
If this happens please modify the files to adhere to the code style, add them to the staging area, and then retry to execute the commit.

The hooks are configured with the tool [pre-commit](https://pre-commit.com) through the `.pre-commit-config.yaml` file. Please check the [Adding plugins](https://pre-commit.com/#plugins) page for the correct syntax and the [Supported hooks](https://pre-commit.com/hooks.html) page for a list of ready to use hooks.

#### Enabling Pre-Commit Hooks

In order to enable the pre-commit please don't skip the `pre-commit install` step in [Development Installation](#development-installation).

> **Warning**: If using a Git GUI please verify that Git hooks are a compatible feature before using it for commits. We verified that our recommended IDE VS Code correctly works with them.

#### Update the Hooks Version

The specific version of each hook, specified in `.pre-commit-config.yaml`, can be updated to the latest release with the command:

```bash
pre-commit autoupdate
```

Since some of the packages specified in `.pre-commit-config.yaml` are also present in `setup.py`, when updating versions please verify they are matching in both files.

### Unit Tests

Template Project tests are located under `tests/`.

We support the `pytest` framework, see its [home page](https://docs.pytest.org/en/latest/index.html) for more details.

To run all tests you can simply run:
```bash
pytest -ra
```

#### Test Coverage Reports

To get coverage reports we recommend using [pytest-cov](https://pypi.org/project/pytest-cov/).

With the following command you can get an HTML report, available in `htmlcov/index.html`, showing the percentage of statements executed for each source file in the template_project package while running the tests:

```bash
pytest --cov=template_project --cov-report=html -ra
```

You can navigate the pages in the HTML report to analyze which lines have never been executed and notes on possible issues.

With the following command you can get a similar report for branch coverage, checking if every possible branch in the program has been executed at least once:

```bash
pytest --cov=template_project --cov-report=html --cov-branch -ra
```

It is possible to get a more concise report in the stdout with `--cov-report=term-missing`, or to save a `coverage.xml` file with `--cov-report=xml` that could be useful for coverage tracking tools.
For more advanced usage you can refer to [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/).

### Comments and Docstrings

We use Google style comments and docstrings, see [here](https://google.github.io/styleguide/pyguide.html) for more details.

We write Args etc. like this (hanging indent of 2 spaces):
```python
"""
    Args:
        names: Contact names.
        numbers: Contact telephone numbers.
        surnames: Optional; Contact surnames.
        sep: Optional; Separator used to join first and last names. This parameter is
          ignored if surnames are not provided.
"""
```
and not like this (hanging indent of 4 spaces):
```python
"""
    Args:
        names: Contact names.
        numbers: Contact telephone numbers.
        surnames: Optional; Contact surnames.
        sep: Optional; Separator used to join first and last names. This parameter is
            ignored if surnames are not provided.
"""
```
or this (newline):
```python
"""
    Args:
        names:
            Contact names.
        numbers:
            Contact telephone numbers.
        surnames:
            Optional; Contact surnames.
        sep:
            Optional; Separator used to join first and last names. This parameter is
            ignored if surnames are not provided.
"""
```

We don't specify argument types in the docstrings because we use [type hints](https://www.python.org/dev/peps/pep-0484/).

### Documentation

Template Project's documentation is based on [Sphinx](https://www.sphinx-doc.org/en/master/), a widely used documentation generator for Python projects.

A ready-to-use Sphinx setup can be found in `docs/`, where the project has been configured to auto-generate an API reference parsing the docstrings in the source code. It is very important to follow our guidelines in [Comments and Docstrings](#comments-and-docstrings) as Sphinx was configured to parse this docstring format.
This minimal documentation can be extended writing [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html) pages in .rst source files and saving them to the `docs/` folder, while Sphinx's configuration can be modified acting on `docs/conf.py`.
For more details on how to write documentation using Sphinx please refer to the [official documentation](https://www.sphinx-doc.org/en/master/usage/index.html).

#### How to Build the Documentation

In `scripts/build_docs.sh` we provide an useful script that will update the auto-generated .rst files and build the project's documentation in HTML format in `docs/_build/html`, it can be called from the project's root folder with:

```bash
./scripts/build_docs.sh
```

This script should be included in any CI/CD pipeline, with the built documentation deployed automatically in an accessible dedicated space.

> **Note**: For different reasons it might be preferable to setup Sphinx from scratch instead of relying on the ready-to-use setup. In this case it might be useful following the [Getting Started](https://www.sphinx-doc.org/en/master/usage/quickstart.html) guide from the Sphinx website and then keeping the ready-to-use setup as a reference for configuring the auto-documentation features in `docs/config.py` and in `docs/index.rst`.

#### Deploying the Documentation on Confluence

Sphinx documentation can additionally be deployed in the form of Confluence pages.

This can be done setting two environment variables:

- AP_USER_NAME={Confuence user name}
- AP_USER_SECRET={Confluence password or API key}

And then executing the following command:

```bash
cd docs
rm -rf _autosummary
make confluence
```

If executed correctly, a new page "Enel Template Project" can be found under:
https://confluence.springlab.enel.com/display/DT/Libraries

> **Warning**: The documentation deployment on Confluence should not be executed manually. Confluence documentation is meant to be built automatically by the CI/CD pipeline.

## Our Source-Control Branching Model

### Trunk-Based Development

We follow the [Trunk-Based Development](https://trunkbaseddevelopment.com/) source-control branching model.

In Trunk-Based Development, developers collaborate on code in a single branch called `master` (or trunk), resist any pressure to create other long-lived development branches by employing documented techniques. They therefore avoid merge hell, do not break the build, and live happily ever after.

This new model is a key enabler of **Continuous Integration** and by extension **Continuous Delivery**, and also fit very well with the new microservices design pattern.

Based on the size of the team, the model is further divided into 2 subtypes:
* **Trunk-Based Development**: for smaller team (2/3 developers), the developers commit and push directly on master branch

<img src="https://trunkbaseddevelopment.com/trunk1b.png" alt="flow" width="50%" height="50%"/>

* **Scaled Trunk-Based Development**: for larger teams, developers create short-lived feature branches and once the code on their branch compiles and passes all tests, they merge it directly to the master

<img src="https://trunkbaseddevelopment.com/trunk1c.png" alt="flow" width="50%" height="50%"/>

When our team consists of more than 3 developers we will use the **Scaled Trunk-Based Development**.

### The Flow

The flow in this new model is very easy (see for comparison [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)):
1. Create a new feature branch from the `master` branch. When possibile, each feature branch must respect the format `feature/{JIRA_ISSUE_KEY}` to allow the connection between Jira and the code in Bitbucket
2. Update the *version number* stored in the `__version__` variable located in `src/template-project/__init__.py`. Increment the number following all the [PEP 440](https://www.python.org/dev/peps/pep-0440/#public-version-identifiers) guidelines, in particular we follow the [Semantic Versioning](https://semver.org/) version identification scheme
3. Develop the new feature in the feature branch
4. Make sure your code passes all tests, possibly creating new ones as needed
5. Merge the `master` branch in the feature branch (*Two-Way Merge*), resolve any [merge conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts) and rerun all tests. Eventually update the *version number*
as specified in point 2. (for more information read the chapter *Two developers concurrently doing short-lived feature branches* on [this page](https://trunkbaseddevelopment.com/short-lived-feature-branches/))
6. Create a [git tag](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-tag), for example if the new *version number* is 1.4.0 you can run
    ```bash
    git tag -a v1.4.0 -m "Add multi-GPU support"
    git push --follow-tags
    ```
    Note: push only annotated tags (the above command will not push your tags if they are not annotated)
8. Create a [pull request](https://www.atlassian.com/git/tutorials/making-a-pull-request) on Bitbucket to merge the feature branch into `master`

### Additional Best Practices

In addition to the flow described in the previous chapter, we define a list of best practices following the *trunk based development* advices:
* Don't maintain active a feature branches for more then 2 days (for more information read the documentation about [Short-Lived Feature Branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/))
* Always delete the feature branch after the pull request has been accepted
* When you have been requested to analyze a pull request, try to do it as quickly as possible (if possible within hours of its creation)
* For a possible *long-lived* feature branch or a large-scale change consider to use the [Branch by Abstraction](https://trunkbaseddevelopment.com/branch-by-abstraction/) approach (explained also in this [article](https://martinfowler.com/bliki/BranchByAbstraction.html))
