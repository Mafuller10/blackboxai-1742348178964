from setuptools import setup, find_packages

setup(
    name='classtle',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-login',
        'flask-migrate',
        'flask-bcrypt',
        'python-dotenv',
        'email-validator'
    ]
)