import re
from setuptools import setup, find_packages


version = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", open('echo/__init__.py').read(), re.M).group(1)


setup(
    name='echo',
    version=version,
    packages=find_packages(),
    url='https://github.com/crvernon/echo',
    license='BSD2-Clause',
    author='Chris R. Vernon; Pralit L. Patel',
    author_email='chris.vernon@pnnl.gov',
    description='A Python package to launch ensembles of GCAM runs',
    python_requires='>=3.7.*, <4',
    include_package_data=True,
    install_requires=[
        'numpy>=1.19.4',
        'pandas>=1.1.4',
        'PyYAML>=5.4.1',
        'duckdb>=0.3.1'
    ],
)
