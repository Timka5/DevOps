from setuptools import find_packages, setup

setup(
    name="TradeOpsDE",
    packages=find_packages(exclude=["TradeOpsDE_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
