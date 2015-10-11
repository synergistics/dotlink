from setuptools import setup, find_packages

setup(
    name="dotlink",
    version="1.0",
    description="A lightweight dotfile manager",
    author="Jabari King",
    author_email="kingjak678@gmail.com",
    url="https://github.com/synergistics/dotlink",
    # package_dir={"": "dotlink"},
    # packages=["scripts", "lib"],
    install_requires=[
        'docopt',
        ],
    entry_points={
        "console_scripts": [
            "dotlink = dotlink.main:main",                                 
            ] 
        }
    ) 
