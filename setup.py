try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A game in which you are a mailman deciding which letters to deliver.',
    'author': 'Daniel Maxson',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'vagus.eques@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['letters'],
    'scripts': [],
    'name': 'Letters'
}

setup(**config)