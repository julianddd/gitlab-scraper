from setuptools import find_packages, setup

setup(
    name='gitlab-scraper',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'targets',
        'requests',
        'bs4'
    ],
)