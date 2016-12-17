try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Sam',
    'url': 'https://github.com/SamZhou33/LPTHW',
    'download_url': 'download url'
    'author_email': 'samzhousam@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
