#!/usr/bin/env python

from setuptools import find_packages, setup


def get_version():
    init_py_path = path.join(
        path.abspath(path.dirname(__file__)), "zeroshoteval", "__init__.py"
    )
    init_py = open(init_py_path, "r").readlines()
    version_line = [l.strip() for l in init_py if l.startswith("__version__")][
        0
    ]
    version = version_line.split("=")[-1].strip().strip("'\"")

    return version


setup(
    name="zeroshoteval",
    version=get_version(),
    author="ZSLresearch team",
    url="https://github.com/ZSLresearch-team/ZeroShotEval/",
    description="Python zero-shot learning toolkit",
    install_requires=[
        "yacs>=0.1.6",
        "matplotlib",
        "tqdm>4.29.0",
        "numpy",
        "sklearn",
        "scipy",
        "fvcore",
        "easydict",
        "tensorboard",
        "pandas",
        "simplejson",
    ],
    python_requires=">=3.6",
    extras_require={
        "dev": [
            "flake8==3.8.3",
            "isort",
            "black",
            "flake8-bugbear",
            "flake8-comprehensions",
        ],
    },
    packages=find_packages(exclude=("configs")),
)
