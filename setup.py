"""Installation script for starlight."""
from setuptools import setup, find_packages

setup(
    name='starlight',
    version='1.0',
    description='animated book',
    author='nihlaeth',
    author_email='info@nihlaeth.nl',
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'uvloop',
        'pygame',
        'anime'],
    entry_points={
        'console_scripts': ['starlight = starlight:start']},
    package_data={'starlight': ['images/*', 'story/*']},
    )
