from setuptools import setup
from setuptools import find_packages

setup(
    name=['test_scraper_multiple_pages.py', 'test_scraper_onee_pages.py']
    version='0.0.1',
    description='package that allows you test the scrape_multiple_pages script',
    url='https://github.com/preciousogbeiwi/WebScraper/tree/main/test_scraper',
    author='Precious Ogbeiwi',
    license='',
    packages=find_packages(),
    install_requires=['selenium']



)