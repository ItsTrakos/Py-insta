import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
fh.close()

setuptools.setup(
    name="PyInsta-Scrape",
    version="1.0",
    author="Trakos Pro",
    author_email="mhdeiimhdeiika@gmail.com",
    description="A Python Package Which Scrapes Instagram Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trakos-2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)