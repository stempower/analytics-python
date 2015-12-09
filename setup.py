
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import segment-python module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'segment'))
from segment.analytics.version import VERSION

long_description = '''
Segment is the simplest way to integrate segment analytics into your application.
One API allows you to turn on any other segment analytics service. No more learning
new APIs, repeated code, and wasted development time.

This is the official python client that wraps the Segment REST API (https://segment.com).

Documentation and more details at https://github.com/segmentio/segment-python
'''

setup(
    name='segment-python',
    version=VERSION,
    url='https://github.com/segmentio/segment-python',
    author='Segment',
    author_email='friends@segment.com',
    maintainer='Segment',
    maintainer_email='friends@segment.com',
    test_suite='segment.analytics.test.all',
    packages=['segment','segment.analytics', 'segment.analytics.test'],
    license='MIT License',
    install_requires=[
        'python-dateutil',
        'requests',
        'six'
    ],
    description='The hassle-free way to integrate segment analytics into any python application.',
    long_description=long_description
)
