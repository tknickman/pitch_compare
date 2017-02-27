import os
from setuptools import setup, find_packages


version = '0.0.1'


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid-jinja2',
    'waitress',
    'jsonschema',
    'six',
    'gunicorn'
]

setup(
    name='pitch_compare',
    version=version,
    description='pitch_compare',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Thomas Knickman',
    author_email='tknickman@gmail.com',
    url='www.thomasknickman.com',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="pitch_compare",
    entry_points="""\
        [paste.app_factory]
        main = pitch_compare:main
        """,
)
