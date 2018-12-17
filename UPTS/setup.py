import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="upts_poc",
    version="0.0.5",
    author="Will Wagner",
    author_email="william.wagner@cgu.edu",
    description="A small POC that demonstrates import/export from both databases and .json files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WillWagnerIV/The-Coconuts/tree/master/UPTS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)