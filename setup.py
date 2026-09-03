from setuptools import find_packages, setup
from typing import List

e = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Return the requirements listed in the specified file."""
    requirements = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n"," ") for req in requirments]

    if e in requirements:
        requirements.remove(e)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Tejas",
    author_email="kulkarnitejas.dev@gmail.com",
    packages=find_packages(),
    requires=get_requirements("requirements.txt"),
)