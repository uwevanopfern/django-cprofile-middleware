import re
from distutils.core import setup
from os import path

meta_file = open("django_cprofile_middleware/metadata.py").read()
md = dict(re.findall(r"__([a-z]+)__\s*=\s*'([^']+)'", meta_file))

project_path = path.abspath(path.dirname(__file__))

with open(path.join(project_path, 'README.md')) as f:
    long_description = f.read()


setup(
    name = 'django-cprofile-middleware',
    packages = ['django_cprofile_middleware'],
    license = 'MIT',
    version = md['version'],
    description = 'Easily add cProfile profiling to django views.',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author = md['author'],
    author_email = md['authoremail'],
    url = 'https://github.com/omarish/django-cprofile-middleware/',
    download_url = 'https://github.com/omarish/django-cprofile-middleware/tarball/v1.0',
    keywords = ['django','profiling','cProfile'],
    classifiers = [
        "Framework :: Django"
    ],
)
