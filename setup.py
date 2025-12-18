
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    """
    This function reads the requirements from a file and returns a list of packages.
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        # Remove any whitespace and newlines
        requirements = [req.replace('\n','') for req in requirements ]

        # Remove the '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


    
    
    return requirements

setup(
    name='ML-Project-1',
    version='0.0.1',
    author='Kartik Sharma',
    author_email='kartiksharma1227@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)