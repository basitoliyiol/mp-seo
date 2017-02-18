
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-mp-seo',
    version='1.0',
    description='Django seo app',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-seo',
    download_url='https://github.com/pmaigutyak/mp-seo/archive/1.0.tar.gz',
    packages=['seo'],
    license='MIT',
    install_requires=[
        'django-modeltranslation==0.11'
    ]
)
