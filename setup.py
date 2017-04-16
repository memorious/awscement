from distutils.core import setup

setup(
    name='awscement',
    version='1.0.0',
    author='Memorious',
    author_email='memorious@modulismo.com',
    packages=['awscement','awscement.s3'],
    scripts=['bin/s3interface'],
    url='https://github.com/memorious/awscement',
    license='LICENSE.txt',
    description='Useful command line tools for CRUD of some AWS resources.',
    long_description=open('README.txt').read(),
    install_requires=[
        "cement > 1.0.0"
    ],
)
