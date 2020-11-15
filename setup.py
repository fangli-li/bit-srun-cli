from setuptools import setup, find_packages

setup(
    name='srun-bit',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Requests',
    ],
    entry_points='''
        [console_scripts]
        srun-bit=cli.cli:cli
    ''',
)