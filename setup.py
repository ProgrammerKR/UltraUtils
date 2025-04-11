from setuptools import setup, find_packages

setup(
    name="UltraUtils",
    version="1.0.0",
    packages=find_packages(include=["ultrautils", "ultrautils.*"]),
    description="A Python utility library with string, math, file, and more utilities.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Prog. Kanishk Raj",
    author_email="programmerkr.123@gmail",
    url="https://github.com/ProgrammerKR/UltraUtils",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
)
