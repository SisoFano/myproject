from setuptools import setup, find_packages

setup(
    name='myproject',
    version='0.4',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA project',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com:SisoFano/myproject',
    author='SisoFano',
    author_email='sisofano@gmail.com'
)
