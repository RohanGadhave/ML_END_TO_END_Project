from setuptools import find_packages, setup
from typing import List


HYPEN__spa_dot ='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN__spa_dot in requirements:
            requirements.remove(HYPEN__spa_dot)
    return requirements
setup(

    name="my_package",
    version="0.1.0",    
    author="Rohan Gadhave",
    author_email="rohangadhave1997@gmail.com",
    description="A sample Python package",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)