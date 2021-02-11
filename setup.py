from setuptools import setup, find_packages
import versioneer

# To use a consistent encoding
from codecs import open
from os import path

cur_dir = path.abspath(path.dirname(__file__))

with open(path.join(cur_dir, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='actions_test',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='hhslepicka',
    packages=find_packages(),
    description='Test Project for GHActions', 
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hhslepicka/actions_test',
    license='BSD',
)
