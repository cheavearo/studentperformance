from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    """
    This function will return the list of project requirements.
    """
    requirements = []
    with open(file_path) as files:
        requirements = files.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

            
    

setup(
    name='studentperformance',
    version='0.0.1',
    author='C.Vearo',
    author_email='vearochea8@gmail.com',
    packages=find_packages(),
    install_requres = get_requirements(file_path='requirements.txt')

)