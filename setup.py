from setuptools import setup, find_packages

setup(
    name="ships",
    version="1.0.0",
    description="A tool to convert webpages to ASCII structure.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="syeasar",
    author_email="syeasar.kuet@gmail.com",
    url="https://github.com/y3454r/ships",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ships = ships.cli:main",
        ],
    },
    install_requires=[
        "requests",
        "html2text",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
