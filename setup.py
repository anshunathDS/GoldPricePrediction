from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requiremets=file_obj.readlines()
        requiremets=[req.replace("\n","") for req in requirements]
        return requiremets


setup(
name='GoldPricePrediction',
version='0.0.1',
author='Anshu',
author_email='anshunath007@gmail.com',
install_requires=get_requirements('requirements.txt'),
packages=find_packages()

)