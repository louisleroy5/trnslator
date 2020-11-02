# To use a consistent encoding
import codecs
import re
import sys
import os
from os import path

# Always prefer setuptools over distutils
from setuptools import setup

here = os.getcwd()

# This check is here if the user does not have a new enough pip to recognize
# the minimum Python requirement in the metadata.
if sys.version_info < (3, 6):
    error = """
trnslator 1.0+ does not support Python 2.x, 3.0, 3.1, 3.2, or 3.3.
Python 3.6 and above is required. This may be due to an out of date pip.
Make sure you have pip >= 9.0.1.
"""
    sys.exit(error)


def read(*parts):
    with codecs.open(path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the README file
with codecs.open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt")) as f:
    requirements_lines = f.readlines()
install_requires = [r.strip() for r in requirements_lines]

with open(path.join(here, "requirements-dev.txt")) as f:
    requirements_lines = f.readlines()
dev_requires = [r.strip() for r in requirements_lines]

setup(
    name="trnslator",
    version=find_version("trnslator", "__init__.py"),
    packages=["trnslator"],
    package_data={
        "trnslator": [
            "trnslator/ressources/originBUISketchUp.idf",
            "trnslator/ressources/W74-lib.dat",
            "trnslator/ressources/NewFileTemplate.d18",
        ]
    },
    include_package_data=True,
    url="https://github.com/louisleroy5/trnslator",
    license="-",
    author="Louis Leroy",
    author_email="louis.leroy@polymtl.ca",
    description="Convert IDF file (EnergyPlus) to BUI file (TRNBuild)",
    long_description=long_description,
    keywords="Building archetypes",
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    test_suite="tests",
    entry_points="""
        [console_scripts]
        trnslator=trnslator.cli:cli
    """,
)
