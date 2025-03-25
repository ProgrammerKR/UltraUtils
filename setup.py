from setuptools import setup, find_packages

setup(
    name="UltraUtils",
    version="1.0.0",
    author="Kanishk Raj",
    author_email="your-email@example.com",
    description="A powerful Python utility library with string, file, math, datetime, list, dict, random, and system utilities.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourgithub/UltraUtils",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.6",
    keywords="utilities, helper functions, python utilities, ultrautils",
)
