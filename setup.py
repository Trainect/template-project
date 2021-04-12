import os
import re

from setuptools import find_packages, setup

DOC_REQUIRES = [
    "m2r2==0.2.7",
    "sphinx==3.5.3",
    "sphinx-autodoc-typehints==1.11.1",
    "sphinx-rtd-theme==0.5.1",
    "sphinxcontrib.confluencebuilder==1.4.0",
]
TEST_REQUIRES = ["pytest", "pytest-cov"]
DEV_REQUIRES = (
    DOC_REQUIRES
    + TEST_REQUIRES
    + [
        "black==20.8b1",
        "flake8==3.8.4",
        "isort==5.6.4",
        "mypy==0.790",
        "pre-commit",
    ]
)

# get version string from module
with open(
    os.path.join(os.path.dirname(__file__), "src", "template_project", "__init__.py"),
    "r",
) as f:
    pattern = r"__version__ = ['\"]([^'\"]*)['\"]"
    version = re.search(pattern, f.read(), re.M).group(1)  # type: ignore

setup(
    name="enel-template-project",
    version=version,
    author="Enel S.p.A.",
    description="Template for the Python repositories of the ODIN program",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"template_project": ["py.typed"]},
    install_requires=["pandas"],
    extras_require={"dev": DEV_REQUIRES, "doc": DOC_REQUIRES, "test": TEST_REQUIRES},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    zip_safe=False,
)
