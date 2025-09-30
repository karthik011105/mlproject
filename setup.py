from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements.txt and return a clean list of dependencies.
    Removes '-e .' if present.
    """
    requirements: List[str] = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # removes \n etc.

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='ml_project1',
    version='0.0.1',
    author='vk',
    author_email='k.v.karthik1105@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
