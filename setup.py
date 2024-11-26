from setuptools import setup, find_packages

setup(
    name="num-word-converter",
    version="1.0.6",
    packages=find_packages(),

    # Metadata
    author="Vladyslav Lazoryk",
    author_email="lazorkinv@gmail.com",
    description="A package to convert numbers to words and vice-versa",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
)
