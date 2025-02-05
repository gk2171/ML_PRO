from setuptools import find_packages, setup
from typing import List 

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements.
    '''
    requirements = []
    with open(file_path, "r", encoding="utf-8") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Fix list comprehension

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name="ml_project",  # Fixed whitespace issue
    version="0.0.1",
    author="GK",
    author_email="gopalakrishnan2124@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
