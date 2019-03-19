from setuptools import setup, find_packages

setup(
    name='myproject',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA project',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='git@github.com:SisoFano/myproject.git',
    author='<SisoFano>',
    author_email='<sisofano@gmail.com>'
)
