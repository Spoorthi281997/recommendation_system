from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='recommendation_system',
    packages=find_packages(),
    version='0.1.0',
    description='Personalized recommendations of Products to Users',
    long_description=readme,
    author='Spoorthi Chinivar',
    author_email='chinivarspoorthi@gmail.com'
    license=license,
    url='https://github.com/Spoorthi281997/recommendation_system'
)

