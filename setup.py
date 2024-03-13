import setuptools
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'CT-kidney-tumor-classification'
AUTHOR_USER_NAME = 'vinaykadam007'
SRC_REPO ='cnnClassifier'
AUTHOR_EMAIL = 'vinay0745@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A python package for kidney tumor classification',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}'

)