import os

from setuptools import find_packages, setup

with open(os.path.join("pybullet_envs_gymnasium", "version.txt")) as file_handler:
    __version__ = file_handler.read().strip()


setup(
    name="pybullet_envs_gymnasium",
    packages=[package for package in find_packages() if package.startswith("pybullet_envs_gymnasium")],
    package_data={
        "pybullet_envs_gymnasium": [
            "py.typed",
            "version.txt",
        ]
    },
    install_requires=["pybullet>=3.2.5", "gymnasium>=0.28.1,<1.0"],
    extras_require={},
    description="Gymnasium port of pybullet envs",
    author="Antonin Raffin",
    url="",
    author_email="antonin.raffin@dlr.de",
    keywords="",
    license="zlib",
    long_description="",
    long_description_content_type="text/markdown",
    version=__version__,
    python_requires=">=3.8",
    # PyPI package information.
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
