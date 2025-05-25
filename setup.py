from setuptools import setup, find_packages
from typing import List

HEPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    It removes any version specifiers and comments.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HEPEN_E_DOT in requirements:
            requirements.remove(HEPEN_E_DOT)
    
    return requirements

setup(
    name='ml-project',
    version='0.0.1',
    author='Yagnik',
    email='anyuse05@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
)