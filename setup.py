from setuptools import find_packages , setup 
from typing import List

hyphon_e_dot = '-e .'
def get_Requirments(file_path:str)->List[str]:
    '''this will return requirments.txt'''
    requirments=[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","") for req in requirments]
        if hyphon_e_dot in requirments:
            requirments.remove(hyphon_e_dot)
    return requirments
        
setup(
    name='Mlproject',
    version='0.0.1',
    author='Aniket',
    author_email='surajsinghhh1342@gmail.com',
    packages=find_packages(),
    install_requires=get_Requirments('requirments.txt')
    
)