
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-mp-seo',
    version='1.1',
    description='Django seo app',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-seo',
    download_url='https://github.com/pmaigutyak/mp-seo/archive/1.1.tar.gz',
    packages=['seo'],
    license='MIT',
    install_requires=[
        'django-modeltranslation==0.11'
    ]
)
