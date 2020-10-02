import setuptools
import os
import re

PACKAGE_NAME="reusable"

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, PACKAGE_NAME, "__init__.py"), "r") as init_file:
    init_content = init_file.read()
attrs = dict(re.findall(r"__([a-z]+)__ *= *['\"](.+)['\"]", init_content))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=attrs['version'],
    author=attrs['author'],
    author_email="ohidurbappy+reusable@gmail.com",
    description="Python reusable code and utility classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ohidurbappy/reusable",
    include_package_data=True,
    platforms="any",
    packages=setuptools.find_packages(),
    package_data={PACKAGE_NAME: ['data/*.txt']},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.5',
)
