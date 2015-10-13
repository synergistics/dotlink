from setuptools import setup, find_packages

setup(
    name="dotlink",
    version="0.0",
    description="A lightweight dotfile manager",
    author="Jabari King",
    author_email="kingjak678@gmail.com",
    url="https://github.com/synergistics/dotlink",
    packages=find_packages(),
    package_data={"dotlink": ["commands_docs/*.txt"]},
    py_modules=["dotlink.relevancedict"],
    install_requires=[
        "docopt",
        ],
    entry_points={
        "console_scripts": [
            "dotlink = dotlink.main:main",                                 
            ] 
        }
    ) 
