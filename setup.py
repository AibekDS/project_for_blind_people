from setuptools import find_packages, setup

setup(
    name='hacaton_project',
    package_dir={'': 'src'}
    packages=find_packages('src'),
    version='0.1.0',
    description='I made a project through computer vision to help blind people on the street.',
    author='Aibek',
    license='MIT',
)
