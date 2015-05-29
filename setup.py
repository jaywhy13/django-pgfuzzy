import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pgfuzzy',
    version='0.1',
    packages=['pgfuzzy'],
    include_package_data=True,
    license='GPL v3 License',  # example license
    description='A set of lookups for Django to allow usage of PostgreSQL fuzzystrmatch extension',
    long_description=README,
    url='http://github.com/codedbyjay/django-pgfuzzy',
    author='Jean-Mark Wright',
    author_email='jeanmark.wright@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[ req for req in open("%s/requirements.txt" % os.path.abspath(os.path.dirname(__file__)),"r").read().splitlines() if req.strip() and not req.startswith("#")]
)