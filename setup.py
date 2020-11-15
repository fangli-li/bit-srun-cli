from setuptools import setup, find_packages

DESCRIPTION = 'A cli to login BIT network.'
AUTHOR = 'Fang Li'
EMAIL = 'fangli-li@qq.com'
REQUIRES_PYTHON = '>=3.6.0'
URL = 'https://github.com/fangli-li/bit-srun-cli'

setup(
    name='srun-bit',
    version='0.1',
    packages=find_packages(),
    description=DESCRIPTION,
    include_package_data=True,
    author=AUTHOR,
    url=URL,
    install_requires=[
        'Click',
        'Requests',
    ],
    entry_points='''
        [console_scripts]
        srun-bit=cli.cli:cli
    ''',
)