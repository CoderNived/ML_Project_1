from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

    # Remove '-e .' if present
    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements

setup(
    name='NEW_ML_PROJECT_1',
    version='0.0.1',
    author='Nived',
    author_email='nivedshenoy0@gmail.com',
    packages=find_packages(where="src"),   # 👈 tell setuptools to search in src/
    package_dir={"": "src"},               # 👈 map root to src/
    install_requires=get_requirements('requirements.txt')
)
