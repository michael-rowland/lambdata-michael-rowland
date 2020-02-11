from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-michael-rowland",
    version="0.1",
    author="Michael Rowland",
    author_email="mrowland13@gmail.com",
    description="Starter package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/michael-rowland/lambdata-michael-rowland",
    keywords="lambda school",
    packages=find_packages() # ["my_lambdata"]
)
