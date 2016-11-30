from setuptools import setup


setup(
    name='amqp-middleware',
    version='1.0',
    description='AMQP Consumer-Publisher Middleware',
    url='https://github.com/pchristos/amqp-middleware',
    license='Apache',
    author='Chris Pollalis',
    author_email='cpollalis@mist.io',
    packages=['amqpconsumer'],
    entry_points={
        'console_scripts': [
            'amqp-middleware = amqpconsumer.components.agent:bootstrap',
        ],
    },
    dependency_links=[
        'git+https://github.com/pchristos/amqp-middleware.git@master#egg=amqp-middleware',
    ],
    install_requires=[
        'pika>=0.9.14',
        'ws4py==0.3.5',
        'requests==2.7.0',
    ],
)
