from setuptools import setup, find_packages

setup(
    name="py8ite",
    version="1.0.0",
    packages=find_packages(),
    author="itnovre",
    description="The Ultimate Python Utility Function that transforms your Python environment",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/itnovre/py8ite",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    keywords="utility, development, enhancement, debugging",
)