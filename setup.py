from setuptools import setup, find_packages

setup(
    name="cloudquicklabs1",
    version="0.0.3",
    author="Rekhu Chinnarathod",
    author_email="vrchinnarathod@gmail.com",
    url="https://www.youtube.com/channel/UCv9MUffHWyo2GgLIDLVu0KQ",
    description="An application that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["cloudquicklabs1 = src.main:main"]},
)