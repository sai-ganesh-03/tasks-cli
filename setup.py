from setuptools import setup

setup(
    name='task-cli-project',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        task-cli=main:cli
    ''',
)
