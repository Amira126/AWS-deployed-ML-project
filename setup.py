from setuptools import find_packages, setup

Hyphen_e_dot = '-e .'

def get_requirements(file_path:str):
    '''
    Function to return the requirements list
    '''
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '')for req in requirements]

        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)

    return requirements


setup(
name='MLproject',
version='0.0.1',
author='Amira Abdelrahman',
author_email='amiramahmoud987@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)