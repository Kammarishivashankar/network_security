
from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """returns list of requirements."""

    try:
        requirement_lst:List[str] = []
        with open('requirements.txt','r') as file:
            lines  = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e.':
                    requirement_lst.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt file not found!")

    return requirement_lst

setup(

    name = "NetwrokSecurity",
    version = "0.0.1",
    author = "ShivaShankar",
    author_email = "Kammarishivashankar2023@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements(),
)

