"""Setup file for Mini Matlab clone app."""

import re
from setuptools import setup


REQUIRES = [
    'prompt-toolkit',
    'numpy',
    'pygments'
]


def find_version(fname):
    """"Attempt to find the version number in the file names fname.

    :fname: the file name
    Raises RuntimeError if not found.
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("mini_matlab/mini_matlab.py")


def read(fname):
    """Read from file.

    :fname: the file name
    """
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='mini_matlab',
    version="0.0.1",
    description='Mini Matlab clone (REPL)',
    long_description=read("README.md"),
    author='Herbert Kagumba',
    author_email='habukagumba@gmail.com',
    url='https://github.com/Habu-Kagumba/mini_matlab',
    install_requires=REQUIRES,
    license=read("LICENSE"),
    zip_safe=False,
    keywords='mini_matlab',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
    ],
    py_modules=["mini_matlab"],
    entry_points={
        'console_scripts': [
            "minimatlab = mini_matlab.mini_matlab:main"
        ]
    },
    tests_require=['nose'],
    test_suite='nose.collector'
)
