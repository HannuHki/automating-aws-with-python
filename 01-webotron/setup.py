from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='HH',
    author_email='hannu_hautamaki@hotmail.com',
    description='Webotron 80 is a tool to deploy.',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
