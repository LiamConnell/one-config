from setuptools import setup, find_packages

VERSION = '0.2.2'

with open("README.md", "r") as fh:
    README = fh.read()


setup(
    name="one-config",
    version=VERSION,
    description="A universally accessible config object that only has to be constructed once",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/LiamConnell/one-config",
    author="LiamConnell",
    # author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=["PyYAML"],
    # entry_points={
    #     "console_scripts": [
    #         "realpython=reader.__main__:main",
    #     ]
    # },
)