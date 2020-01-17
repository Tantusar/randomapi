from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'randomapi',
    version = '0.3',
    description = 'RANDOM.org JSON-RPC API implementation',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Mitchell Cohen <mitch.cohen@me.com>',
    author_email = 'mitch.cohen@me.com',
    maintainer = 'Thomas Chick (twitter.com/Tantusar)',
    py_modules = ['randomapi'],
    url = 'https://github.com/Tantusar/randomapi',
    license = 'MIT License',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.6',
    download_url = 'https://github.com/Tantusar/randomapi/archive/v0.3.tar.gz'
)
